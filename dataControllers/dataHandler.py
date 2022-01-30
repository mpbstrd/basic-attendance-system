import random
from fileHandler import theFile
from teacher import Teacher
from department import Department


print()
f = theFile()

inputID = input("ID:" )
t = Teacher()
temp = t.idExists(str(inputID))

print(temp)