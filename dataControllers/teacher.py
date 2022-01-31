import json
import os
from dataControllers.fileEncryptionDecryption import fileEncrypt
from fileHandler import theFile as UserFiles
from fileEncryptionDecryption import fileEncrypt
from fileEncryptionDecryption import fileDecrypt
class Teacher:
    name=""
    did=-1
    tid=-1

    # def __init__(self, tid, name, did):
    def __init__(self, *args):
        if len(args)>0:
            self.tid=args[0]
            self.name=args[1]
            self.did=args[2]
            self.encrypted=False

    def setTeacher(self, tid, name, did):
        self.tid=tid
        self.name=name
        self.did=did

    def addTeacher(self):
        data = {}
        f = UserFiles()

        # ADD NEW TEACHER TO JSON
        try:
            handler = UserFiles()
            file = handler.t_file

            with open(file, 'r+') as teacherFile:

                if self.encrypted == True:
                    fileDecrypt(teacherFile)
                    self.encrypted = False

                data = json.load(teacherFile)
                newTeacher = {str(self.tid): {'name': self.name, 'id':self.tid, 'did':self.did}}
                data.update(newTeacher)

            with open(file, 'w+') as teacherFile:
                
                if self.encrypted != True:
                    fileDecrypt(teacherFile)
                    self.encrypted = True

                json.dump(data, teacherFile, indent=4)

            # UPDATE TEACHER COUNT FROM META DATA
            f.metaAddTeach()

            return True
        except Exception as e:
            return e
        

    def getTeacherID(self):
        return self.tid
        
    def idExists(self, id):
        try:
            handler = UserFiles()
            file = handler.t_file

            with open(file, 'r+') as teacherFile:
                data = json.load(teacherFile)

                if type(data[id]) == type({}):
                    return True
                else:
                    return False
        except Exception as e:
            return e
