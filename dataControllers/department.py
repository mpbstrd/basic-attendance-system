import json
import os
from fileHandler import theFile as UserFiles
from fileEncryptionDecryption import fileEncrypt
from fileEncryptionDecryption import fileDecrypt

class Department:
    name=""
    id=-1

    

    def __init__(self, id, name):
        self.id=id
        self.name=name
        self.encrypted = False

    def addDepartment(self):
        data = {}
        f = UserFiles()

        # ADD NEW DEPARTMENT TO JSON
        try:
            handler = UserFiles()
            file = handler.d_file

            with open(file, 'r+') as departmentFile:
                
                if self.encrypted == True:
                    fileDecrypt(departmentFile)
                    self.encrypted = False

                data = json.load(departmentFile)
                newDept = {str(self.id): {'name': self.name, 'id':self.id}}
                data.update(newDept)

            with open(file, 'w+') as departmentFile:
                
                if self.encrypted != True:
                    fileDecrypt(departmentFile)
                    self.encrypted = True

                json.dump(data, departmentFile, indent=4)

            # UPDATE DEPARTMENT COUNT FROM META DATA
            f.metaAddDept()

            return True
        except Exception as e:
            return e
        

    def getDepartmentID(self):
        return self.tid
        
