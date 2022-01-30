import os
from re import T
import tempfile

class theFile:

    # Sub-dir of each directories
    # Parent folder
    p = "Attendance"

    # Data folder 
    j = os.path.join("C:\\", p, "Data")

    # Files
    t = os.path.join(j, "TeacherList")
    d = os.path.join(j, "DepartmentList")
    a = os.path.join(j, "AttendanceList")

    def createDirs(self):

        try:
            pHold = os.path.join(self.p,self.j)

            if os.path.isdir(pHold) != True:
                os.makedirs(pHold)
                print("Directories created!")

        except Exception as e:
            print(e)

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
            
            print("Files created!")
            
        except Exception as e:
            print(e)