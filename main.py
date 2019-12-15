from game import Game, Player

username = 'none'
startingCash = 500

def displayPlayerCash(username):
    print("CASH: {}".format(username.cash))

lon = input("New game? [y/n] ")
if lon == 'y':
    username = input("Username: ")
    player = Player(username, startingCash)
    player.savePlayerData()
elif lon == 'n':
    print("loading saved data...\n\n")
    player = Player('loading', 0)
    if player.loadPlayerData() == False:
        print("No save data. Starting new game...")
        username = input("Username: ")
        player.playerUsername_set(username)
    else:
        pass
    player.savePlayerData()

game = Game(player.username)
game.initStartup()
displayPlayerCash(player)
