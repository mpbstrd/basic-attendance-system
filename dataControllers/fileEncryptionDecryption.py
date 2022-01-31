import base64
import os
import cryptography
from random import choice
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def createKey():
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_provided = ''.join(choice(string) for i in range(12))
    password = password_provided.encode() #Convert to type bytes

    salt = b'\xa9!\xf0\xcc\x94&[\xc4\xf4\xac\x0f)=\x160\xf5'

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), 
                    length=32, 
                    salt=salt, 
                    iterations=100000, 
                    backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password)) #Can only use kdf once
    return key

def fileEncrypt(input_file):
    keygen = createKey() 
    output_file = os.path.splitext(input_file)[0] + ".enc"
    key = os.path.splitext(input_file)[0] + ".key"

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the input file

    fernet = Fernet(keygen , "b")
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)  # Write the encrypted bytes to the output file
        if os.path.exists(input_file):
            os.remove(input_file)
    with open(key, 'wb') as f:
        f.write(keygen)
        
    # Note: You can delete input_file here if you want

def fileDecrypt(input_file,filekey):
    output_file = os.path.splitext(input_file)[0] + ".json"

    with open(filekey, 'rb') as rawkey:
        key = rawkey.read()  # Read the bytes of the encrypted file

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key , 'b')
    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)  # Write the decrypted bytes to the output file
            if os.path.exists(input_file):
                os.remove(input_file)

        # Note: You can delete input_file here if you want
    except (cryptography.fernet.InvalidToken, TypeError):
        print("Decryption Failed: Invalid key")