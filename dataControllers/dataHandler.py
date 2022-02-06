import random
from fileHandler import theFile
from teacher import Teacher
from department import Department
from attendance import Attendance
from fileEncryptionDecryption import fileEncrypt
from fileEncryptionDecryption import fileDecrypt
from teacher import idExists



print()
f = theFile()

inputID = input("ID:" )
t = Teacher()
# temp = idExists(inputID)

a = Attendance()
# print(temp)
fileEncrypt(f.t_file)
#print(a.timein(inputID))
#print(a.timeout(inputID))

