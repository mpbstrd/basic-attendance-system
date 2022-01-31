from asyncio.windows_events import NULL
import json
import os
from fileHandler import theFile as UserFiles
from datetime import date
from datetime import time
from datetime import datetime
from fileEncryptionDecryption import fileDecrypt as decrypt
from fileEncryptionDecryption import fileEncrypt as encrypt

class Attendace:
    def __init__(self):
        print("asdasd")

    def timein(self, id):
        self.id = id
        data = {}
        f = UserFiles()
        now = datetime.now()

        # ADD NEW TEACHER TO JSON
        handler = UserFiles()
        file = handler.a_file
        
        today = now.strftime("%Y/%m/%d")
        self.time_in = now.strftime('%I:%M:%S %p')

        with open(file, 'r+') as attFile:

            if self.encrypted == True:
                decrypt(attFile)
                self.encrypted = False

            data = json.load(attFile)

            # ti = {'id': self.id, "time_in": self.time_in , "time_out": data[today]["time_out"]}

            ti = {'id': self.id, "time_in": self.time_in , "time_out": NULL}
            newAtt = {today: ti}

            data.update(newAtt)

            with open(file, 'w+') as attFile:

                if self.encrypted != True:
                    decrypt(attFile)
                    self.encrypted = True

                json.dump(data, attFile, indent=4)

        return data
        
        
    def timeout(self, id):
        self.id = id
        data = {}
        f = UserFiles()
        now = datetime.now()

        # ADD NEW TEACHER TO JSON
        handler = UserFiles()
        file = handler.a_file
        
        today = now.strftime("%Y/%m/%d")
        self.time_out = now.strftime('%I:%M:%S %p')

        with open(file, 'r+') as attFile:
            data = json.load(attFile)

            # ti = {'id': self.id, "time_in": self.time_in , "time_out": data[today]["time_out"]}

            ti = {'id': self.id, "time_in": data[today]["time_in"] , "time_out": self.time_out}
            newAtt = {today: ti}

            data.update(newAtt)

            with open(file, 'w+') as attFile:
                json.dump(data, attFile, indent=4)

        return data