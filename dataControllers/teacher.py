import json
import os
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
            file = handler.tenc_file

            if self.encrypted == True:
                fileDecrypt(file)
                self.encrypted = False

            with open(file, 'r+') as teacherFile:
                data = json.load(teacherFile)
                newTeacher = {str(self.tid): {'name': self.name, 'id':self.tid, 'did':self.did}}
                data.update(newTeacher)
            
            with open(file, 'w+') as teacherFile:
                json.dump(data, teacherFile, indent=4)

            if self.encrypted != True:
                fileEncrypt(handler.a_file)
                self.encrypted = True
            # UPDATE TEACHER COUNT FROM META DATA
            f.metaAddTeach()

            return True
        except Exception as e:
            return e
        

    def getTeacherID(self):
        return self.tid
        
def idExists(id):
    try:
        handler = UserFiles()
        file = handler.t_file
        efile = handler.tenc_file

        fileDecrypt(efile)
        
        with open(file, 'r+') as teacherFile:
            data = json.load(teacherFile)
            
            fileEncrypt(efile)

            if type(data[id]) == type({}):
                return True
            else:
                return False

    except Exception as e:
        return e
