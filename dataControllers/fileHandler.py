import os
import json

class theFile:

    # Sub-dir of each directories
    # Parent folder
    p = "Attendance"

    # Data folder 
    j = os.path.join("C:\\", p, "Data")

    # Files
    meta = os.path.join("C:\\", p, "meta.json");
    t_file = os.path.join(j, "TeacherList.json")
    d_file = os.path.join(j, "DepartmentList.json")
    a_file = os.path.join(j, "AttendanceList.json")
    tenc_file = os.path.join(j, "TeacherList.enc")
    denc_file = os.path.join(j, "DepartmentList.enc")
    aenc_file = os.path.join(j, "AttendanceList.enc")

    # Initializes all folders
    def createDirs(self):

        try:
            pHold = os.path.join(self.p,self.j)

            if os.path.isdir(pHold) != True:
                os.makedirs(pHold)
                return True
        except Exception as e:
            return e

        try:
            with open(os.path.join(self.j, "TeacherList.json"), 'wb') as temp_file:
                temp_file.write(b"{}")
                temp_file.close()
                
            with open(os.path.join(self.j, "DepartmentList.json"), 'wb') as temp_file:
                temp_file.write(b"{}")
                temp_file.close()
                
            with open(os.path.join(self.j, "AttendanceList.json"), 'wb') as temp_file:
                temp_file.write(b"{}")
                temp_file.close()
            
            return True    
        except Exception as e:
            return e

    # Initiates meta data
    def createMeta(self):
        newC={}

        try:
            with open(self.meta, 'wb') as m:
                m.write(b"{}")
                m.close()

            with open(self.meta, 'r') as m:
                c = json.load(m)
                newC = {"teacher-count": 0, "department-count": 0}
                c.update(newC)
                m.close()

            with open(self.meta, 'w') as m:
                json.dump(newC, m, indent=4)
                m.close

            
            return True    
        except Exception as e:
            return e
            
    # Updates Department count on meta data
    def metaAddDept(self):
        try:
            with open(self.meta, 'r') as d:
                c = json.load(d)
                newC = {"department-count": c.get("department-count")+1, "teacher-count": c.get("teacher-count")}
                c.update(newC)
                d.close()

            with open(self.meta, 'w+') as d:
                json.dump(newC, d, indent=4)
                d.close

            return c.get("department-count")  
        except Exception as e:
            return e

    # Retrieves current Department count
    def getDeptCount(self):
        try:
            with open(self.meta, 'r') as f:
                cf = json.load(f)
                count = cf.get("department-count")
                f.close()

            return count
        except Exception as e:
            return e
            
    # Updates Teacher count on meta data
    def metaAddTeach(self):
        try:
            with open(self.meta, 'r') as t:
                c = json.load(t)
                newC = {"teacher-count": c.get("teacher-count")+1, "department-count": c.get("department-count")}
                c.update(newC)
                t.close()

            with open(self.meta, 'w+') as t:
                json.dump(newC, t, indent=4)
                t.close

            return c.get("teacher-count")  
        except Exception as e:
            return e

    # Retrieves current Teacher count
    def getTeachCount(self):
        try:
            with open(self.meta, 'r') as n:
                cf = json.load(n)
                count = cf.get("teacher-count")
                n.close()

            return count
        except Exception as e:
            return e