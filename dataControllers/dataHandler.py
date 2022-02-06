import random
from fileHandler import theFile
from teacher import Teacher
from department import Department
from attendance import Attendance
from fileEncryptionDecryption import fileEncrypt
from fileEncryptionDecryption import fileDecrypt



print()
f = theFile()

inputID = input("ID:" )
t = Teacher()
temp = t.idExists(str(inputID))

a = Attendance()
# print(temp)

# print(a.timein(inputID))
# print(a.timeout(inputID))

# fileEncrypt(f.t_file)
