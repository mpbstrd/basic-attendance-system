import random
from fileHandler import theFile
from teacher import Teacher
from department import Department
from attendance import Attendace


print()
f = theFile()

inputID = input("ID:" )
t = Teacher()
temp = t.idExists(str(inputID))

# print(temp)

a = Attendace()
print(a.timein(inputID))
print(a.timeout(inputID))

