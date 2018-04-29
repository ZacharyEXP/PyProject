import pickle
from user import *
from task import *
class FileHandler:
    def __init__(self, file):
        self.__file = file
        self.__tasks = []
        #Default testing values
        self.__user = 'no'
        self.__password = 'no'
        self.__name = 'no'
        self.__team = 'no'
        self.__occ = 'no'
        self.__org = 'no'
        self.__strikes = 'no'

    def set_file_path(self, file):
        self.__file = file

    def get_file_path(self):
        return self.__file

    #Strips file for data
    def openFile(self):
        file = open(self.__file, 'r')
        #decoded = pickle.load(file)
        #lines = decoded.readlines()
        lines = file.readlines()
        count = -1

        #Searches file for data and stores it
        for line in lines:
            #print(line + "1")
            count += 1
            new_task = False
            if(line.strip() == '#USER'):
                self.__user = str(lines[count + 1])
            elif(line.strip() == '#PASSWORD'):
                self.__password = str(lines[count + 1])
            elif(line.strip() == '#NAME'):
                self.__name = str(lines[count + 1])
            elif(line.strip() == '#TEAM'):
                self.__team = str(lines[count + 1])
            elif(line.strip() == '#OCCUPATION'):
                self.__occ = str(lines[count + 1])
            elif(line.strip() == '#ORGANIZATION'):
                self.__org = str(lines[count + 1])
            elif(line.strip() == '#STRIKES'):
                self.__strikes = str(lines[count + 1])
            elif(line.strip() != '#TASKEND'):
                #Got weird errors for this part, so code is redundant
                try:
                    if(lines[count].strip().index('$') == 0):
                        self.__objective = str(lines[count].lstrip('$').strip())
                except: 
                    pointlessVar = 0
                
                try:
                    if(lines[count].strip().index('~') == 0):
                        self.__urgency = str(lines[count].lstrip('~').strip())
                except:
                    pointlessVar = 0
                
                try:
                    if(lines[count].strip().index('@') == 0):
                        self.__date_due = str(lines[count].lstrip('@').strip())
                except: 
                    pointlessVar = 0
                
                try:
                    if(lines[count].strip().index('&') == 0):
                        self.__status = str(lines[count].lstrip('&').strip())
                except:
                    pointlessVar = 0

                try:
                    if(lines[count].strip().index('+') == 0):
                        self.__reported = str(lines[count].lstrip('+').strip())
                        new_task = True
                except:
                    pointlessVar = 0
                
            if(new_task):
                self.__tasks.append(Task(self.__date_due, self.__status, self.__objective, self.__urgency, self.__reported))
                new_task = False

        user = User(self.__user, self.__password, self.__name, self.__team, self.__occ, self.__org, self.__strikes, self.__tasks)
        file.close()
        #decoded.close()
        return user

    #Saves user data
    def saveFile(self, user):
        fileOut = open(self.__file, 'w')
        count = 0
        fileOut.truncate()
        fileOut.write("#USER\n")
        fileOut.write(str(user.get_e_id()).strip() + '\n')
        fileOut.write("#PASSWORD\n")
        fileOut.write(str(user.get_password()).strip() + '\n')
        fileOut.write("#NAME\n")
        fileOut.write(str(user.get_name()).strip() + '\n')
        fileOut.write("#TEAM\n")
        fileOut.write(str(user.get_team()).strip() + '\n')
        fileOut.write("#OCCUPATION\n")
        fileOut.write(str(user.get_occ()).strip() + '\n')
        fileOut.write("#ORGANIZATION\n")
        fileOut.write(str(user.get_org()).strip() + '\n')
        fileOut.write("#STRIKES\n")
        fileOut.write(str(user.get_strikes()).strip() + '\n')
        fileOut.write("#TASKSTART\n")
        for task in user.get_tasks():
            fileOut.write('$' + str(task.get_objective().strip()) + '\n')
            fileOut.write('~' + str(task.get_urgency().strip()) + '\n')
            fileOut.write('@' + str(task.get_date_due().strip()) + '\n')
            fileOut.write('&' + str(task.get_status().strip()) + '\n')
            fileOut.write('+' + str(task.get_reported().strip()) + '\n')
            count += 1
        fileOut.write("#TASKEND")
        #pickle.dump(fileOut)
        fileOut.close()
