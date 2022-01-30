import random
from fileHandler import theFile
from teacher import Teacher
from department import Department

j = ".json"
file = "test"

print()
f = theFile()
f.createMeta()
print(f.getDeptCount())
print(f.getTeachCount())


#t = Teacher(1, "", 1)
#print(t.addTeacher())

de = ["Mathematics Department","Science Department","Technological Department","Development Department","English Department","History Department","PE Department","Management Department","Cognitive Science Department","Media Department"]
fn = ["Beverly ","Addie ","Astrid ","Bathilda ","Elvina ","Ida ","Kendra ","Wilfreda ","Sidney ","Imelda "]
sn = ["Lopez","Herrera","Garza","Espinoza","Cuevas","Bernal","Ayala","Arellano","Aguirre","Aguilar"]

max = 10
cur = max-1

for i in range(max):

    t = Teacher(i, fn[i]+sn[i], i)
    print("Teach ID "+str(i)+": "+str(t.addTeacher()))
    print(f.getTeachCount())

    d = Department(i, de[i])
    print("Dept ID "+str(i)+": "+str(d.addDepartment()))
    print(f.getDeptCount())

    
    #print("t: "+str(t.addTeacher())+" | m: "+str(f.metaAddTeach()))

