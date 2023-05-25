import random

def rollDice() :
    return random.randint(1,6)

def above100(playerpos):
    tempPos = 0
    tempPos = playerpos - 100
    playerpos = 100 - tempPos
    return playerpos

def randomingLadder(snl) :
    i = 0
    while i < 7:
        boxindex1 = random.randint(5,90)
        boxindex2 = random.randint(5,90)
        if boxindex1 > boxindex2 :
            while boxindex2 > (boxindex1 / 10) * 10 :
                boxindex2 = random.randint(5,90)
            if not boxindex1 in snl :
                snl[boxindex2] = boxindex1
                print("The bottom of the ladder is at :", boxindex2, "And the top of the ladder is at :", snl[boxindex2])
                i = i + 1
        elif boxindex2 > boxindex1 :
            while boxindex1 > (boxindex2 / 10) * 10 :
                boxindex1 = random.randint(5,90)
            if not boxindex2 in snl :
                snl[boxindex1] = boxindex2
                print("The bottom of the ladder is at :", boxindex1, "And the top of the ladder is at :", snl[boxindex1])
                i = i + 1
        else :
            boxindex1 = random.randint(5,90)
            boxindex2 = random.randint(5,90)
    print("\n")
    return snl

def randomingSnake(snl) :
    i = 0
    while i < 10 :
        boxindex1 = random.randint(10,95)
        boxindex2 = random.randint(10,95)
        if boxindex1 > boxindex2 :
            while boxindex2 > (boxindex1 / 10) * 10 :
                boxindex2 = random.randint(10,95)
            if not boxindex1 in snl :
                snl[boxindex1] = boxindex2
                print("The head of the snake is at :", boxindex1, "And the tail of the snake is at :", snl[boxindex1])
                i = i + 1
        elif boxindex2 > boxindex1 :
            while boxindex1 > (boxindex2 / 10) * 10 :
                boxindex1 = random.randint(10,95)
            if not boxindex2 in snl :
                snl[boxindex2] = boxindex1
                print("The head of the snake is at :", boxindex2, "And the tail of the snake is at :", snl[boxindex2])
                i = i + 1
        else :
            boxindex1 = random.randint(10,95)
            boxindex2 = random.randint(10,95)
    print("\n")
    return snl


def checkingLadderSnake(snl, playerpos) :
    if playerpos in snl:
        if playerpos < snl[playerpos] :
            print("You hit a ladder at", playerpos ,", your position now :", snl[playerpos])
            playerpos = snl[playerpos]
        elif playerpos > snl[playerpos] :
            print("You hit a snake at", playerpos, ", your position now :", snl[playerpos])
            playerpos = snl[playerpos]
    return playerpos

def start() :
    welcomingmessage()
    instructions()
    menu()

def instructions():
    print("--------------------HOW TO PLAY THE GAME-----------------------")
    print('Press \"{}\" to roll the dice and type \"{}\" to stop the game'.format('Enter', 'QUIT'))
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")

def welcomingmessage():
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("--------------Welcome To Snake and Ladder Game------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")

def menu():
    print("\n\nChoose your game mode!!! (1 -> Single Player 2 -> Multiplayer)")
    gamemode = int(input("Input : "))
    snl = {}
    print("")
    randomingLadder(snl)
    randomingSnake(snl)
    if gamemode == 1:
        singleplayer(snl)
    elif gamemode == 2:
        twoplayer(snl)
    
def singleplayer(snl):
    playername = input("Player Name : ")
    playerpos = 0
    play = input()
    while playerpos < 100 and play != 'QUIT':
        dice = rollDice()
        print('Your dice is', dice)
        playerpos += dice
        if playerpos > 100 :
            playerpos = above100(playerpos)
        playerpos = checkingLadderSnake(snl, playerpos)
        print(playername, "Position is at", playerpos, "\n")
        winornot(playerpos, playername)
        play = input()

def twoplayer(snl):
    player1name = input("Player 1 Name : ")
    player2name = input("Player 2 Name : ")
    player1pos = 0
    player2pos = 0
    play = ""
    while (player1pos < 100 and player2pos < 100):
        print(player1name, "turn")
        play = input()
        if play == "QUIT":
            print(player1name, "Position is at", player1pos, "\n")
            print(player2name, "Position is at", player2pos, "\n")
            break
        dice = rollDice()
        print("Your dice is", dice)
        player1pos += dice
        if player1pos > 100:
            player1pos = above100(player1pos)
        player1pos = checkingLadderSnake(snl, player1pos)
        print(player1name, "Position is at", player1pos, "\n")
        winornot(player1pos, player1name)

        print(player2name, "turn")
        play = input()
        if play == "QUIT":
            print("\n", player1name, "Position is at", player1pos, "\n")
            print(player2name, "Position is at", player2pos, "\n")
            break
        dice = rollDice()
        print("Your dice is", dice)
        player2pos += dice
        if player2pos > 100:
            player2pos = above100(player2pos)
        player2pos = checkingLadderSnake(snl, player2pos)
        print(player2name, "Position is at", player2pos, "\n")
        winornot(player2pos, player2name)

def winornot(playerpos, playername):
    if playerpos == 100:
        print(playername, 'Win!')

if __name__ == "__main__":
    start()