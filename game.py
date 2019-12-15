class Game:
    
    def __init__(self, username):
        self.username = username
    
    def displayStartMenu(self):
        menuFileLoc = "C:\\Users\\Brandon\\Anaconda3\\envs\\gambling_game\\menu_title.txt"
        menuGraphic = open(menuFileLoc, 'r')
        for line in menuGraphic:
            if line == '\n':
                pass
            else:
                print(line)
        print("Welcome {}".format(self.username))

    def initStartup(self):
        self.displayStartMenu()

    def displayOptions(self):
        print('1 - Roll Dice')


class Player: 

    def __init__(self, username, startingCash):
        #Saveable data
        #MUST be implemented into the following functions:
        # - updatePlayerData_Variables()
        # - updatePlayerData_Dict()
        #MUST also be created in playerData[] dictionary
        self.cash = startingCash
        self.username = username
        #-------------
        #Used for saving data into the save file
        self.playerData = {
            'username': self.username,
            'cash': self.cash,
            }
        #-------------
        self.saveFileName = "C:\\Users\\Brandon\\Anaconda3\\envs\\gambling_game\\save_data.txt"

    def loadPlayerData(self):
        self.load_temp = []
        saveFile = open(self.saveFileName, 'r')
        for line in saveFile:
            if line == '\n':
                pass
            else:
                self.load_temp.append(line)
        saveFile.close()

        #Checks to make sure the save file does not have too many/little lines in it
        if (len(self.load_temp) > len(self.playerData)):
            print("ERROR: Save file ('{}') overloaded".format(self.saveFileName))
            quit()
        elif (len(self.load_temp) == 0):
            print("No save data!")
            return False
        elif (len(self.load_temp) == len(self.playerData)):
            pass
        elif (len(self.load_temp) < len(self.playerData)):
            print("ERROR: Save file ('{}') underloaded".format(self.saveFileName))
            quit()
        
        #Loads the save data into playerData dict
        #Also makes sure the load_temp data matches value type in playerData dict
        curItem = 0
        for saveKey in self.playerData:
            try:
                self.load_temp[curItem] = type(self.playerData[saveKey])(self.load_temp[curItem])
            except ValueError:
                print("ERROR: invalid value type within save file")
                quit()
            self.playerData[saveKey] = self.load_temp[curItem]
            curItem += 1
        #Crucial so that the data is sent to the necessary variables to be used
        self.updatePlayerData_Variables()

    def savePlayerData(self):
        self.updatePlayerData_Dict()
        saveFile = open(self.saveFileName, 'w')
        for saveKey in self.playerData:
            saveFile.write('{}\n'.format(str(self.playerData[saveKey])))
        saveFile.close()

    #Implements the data from the playerData dict
    def updatePlayerData_Variables(self):
        self.username = self.playerData['username']
        self.cash = self.playerData['cash']
    
    #Takes the data variables and stores them in playerData dict
    def updatePlayerData_Dict(self):
        self.playerData['username'] = self.username
        self.playerData['cash'] = self.cash
    
    def playerCash_change(self, amt):
        self.cash += amt
    
    def playerCash_set(self, amt):
        self.cash = amt
    
    def playerUsername_set(self, username):
        self.username = username
