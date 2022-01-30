import random
from fileHandler import theFile
from teacher import Teacher

j = ".json"
file = "test"

print()
f = theFile
print(f.createMeta(f))

#t = Teacher(1, "", 1)
#print(t.addTeacher())

fn = ["Beverly ","Addie ","Astrid ","Bathilda ","Elvina ","Ida ","Kendra ","Wilfreda ","Sidney ","Imelda "]
sn = ["Lopez","Herrera","Garza","Espinoza","Cuevas","Bernal","Ayala","Arellano","Aguirre","Aguilar"]

max = 10
cur = max-1
for i in range(max-1):

    t = Teacher(i, fn[i]+sn[i], i)
    t.addTeacher()

    #print("t: "+str(t.addTeacher())+" | m: "+str(f.metaAddTeach()))

