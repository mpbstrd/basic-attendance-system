import json
import os
from fileHandler import theFile as UserFiles

class Teacher:
    name=""
    did=-1
    tid=-1

    def __init__(self, tid, name, did):
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

            with open(file, 'r') as teacherFile:
                data = json.load(teacherFile)
                newTeacher = {str(f.getTeachCount): {'name': self.name, 'id':self.tid, 'did':self.did}}
                data.update(newTeacher)

            with open(file, 'w') as teacherFile:
                json.dump(data, teacherFile, indent=4)

            # UPDATE TEACHER COUNT FROM META DATA
            f.metaAddTeach()

            return True
        except Exception as e:
            return e
        

    def getTeacherID(self):
        return self.tid
        
