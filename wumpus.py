import random

#This function is responsible for moving the plater and determining if they ran into something
def movePlayer(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos):
    moveInput = int(input("Where to?"))
    while moveInput not in wumpusMap[playerPos]:
        moveInput = int(input("Not possible - Where to?"))

    if moveInput == bat1Pos or moveInput == bat2Pos:
        moveInput = batLogic()
        while moveInput == bat1Pos or moveInput == bat2Pos:
            moveInput = batLogic()
    if moveInput == hole1Pos or moveInput == hole2Pos:
        moveInput = 21
    if moveInput == wumpusPos:
        moveInput = 22

    return moveInput

#This handles the behavior of the bats
def batLogic():
    print("ZAP--Super Bat snatch! Elsewhereville for you!")
    return random.randint(1,20)

#This tells you about hazards that are nearby
def checkHazards(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos):
    warnings = ""

    if wumpusPos in wumpusMap[playerPos]:
        warnings = warnings + "You smell a wumpus" + "\n"

    if bat1Pos in wumpusMap[playerPos] or bat2Pos in wumpusMap[playerPos]:
        warnings = warnings + "You hear flapping" + "\n"

    if hole1Pos in wumpusMap[playerPos] or hole2Pos in wumpusMap[playerPos]:
        warnings = warnings + "You feel a draft" + "\n"

    return warnings

#This handles arrow shooting logic and what happens if the arrow hits something
def shootArrow(wumpusMap, playerPos, wumpusPos):
    arrowCount = int(input("No. of rooms (1-5)? "))
    arrows = []
    for i in range(arrowCount):
        arrows.append(int(input("Room #?: ")))

    checkArrow = playerPos
    for arrowPos in arrows:
        if arrowPos not in wumpusMap[checkArrow]:
            print("Invalid path! Arrow ricochets...")
            arrowPos = random.choice(wumpusMap[checkArrow])

        if arrowPos == playerPos:
            print("OUCH! Arrow got you!")
            return 1
        if arrowPos == wumpusPos:
            print("AHA! You got the Wumpus!")
            print("You win! The Wumpus is dead!")
            return 2
        checkArrow = arrowPos

    print("Missed.")
    return 3

#This handles the logic when you miss with an arrow
def missedArrow(wumpusMap, playerPos, wumpusPos):
    if random.random() < 0.75:
        print("The Wumpus wakes up!")
        wumpusPos = random.choice(wumpusMap[wumpusPos])
        if wumpusPos == playerPos:
            print("The Wumpus has moved into your room!")
            print("You have been eaten by the Wumpus!")
            return False, wumpusPos
    return True, wumpusPos


def main():
    #the map
    wumpusMap = {
        1: [2,5,8],
        2: [1,3,10],
        3: [2,4,12],
        4: [3,5,14],
        5: [1,4,6],
        6: [5,7,15],
        7: [6,8,17],
        8: [1,7,9],
        9: [8,10,18],
        10: [2,9,11],
        11: [10,12,19],
        12: [3,11,13],
        13: [12,14,20],
        14: [4,13,15],
        15: [6,14,16],
        16: [15,17,20],
        17: [7,16,18],
        18: [9,17,19],
        19: [11,18,20],
        20: [13,16,19]
    }

    arrowCount = 5

    #places objects on map in random locations
    go = True
    while go == True:
        playerPos = random.randint(1, 20)
        bat1Pos = random.randint(1, 20)
        bat2Pos = random.randint(1, 20)
        hole1Pos = random.randint(1, 20)
        hole2Pos = random.randint(1, 20)
        wumpusPos = random.randint(1, 20)

        positions = {playerPos, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos}
        if len(positions) == 6:
            go = False

    #debugging printing
    #print(playerPos, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos)

    print("Welcome to Hunt the Wumpus")

    #main game loop
    playerAlive = True
    while playerAlive == True:
        print(f"\nYou are in room {playerPos}")
        print(f"Tunnels lead to {wumpusMap[playerPos]}")
        print(checkHazards(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos))
        playerIn = input("Shoot, Move or Quit (S-M-Q)?").upper()

        #if you input Q the game ends
        if playerIn == "Q":
            playerAlive = False
            print("Chicken!")

        #if you input S arrow count is decremented and shootArrow is called and results are determined
        elif playerIn == "S":
            arrowCount = arrowCount - 1
            result = shootArrow(wumpusMap, playerPos, wumpusPos)
            if result == 1:
                playerAlive = False
            if result == 2:
                playerAlive = False
            if result == 3:
                #if you miss the arrow missedArrow is called
                playerAlive, wumpusPos = missedArrow(wumpusMap, playerPos, wumpusPos)

            #if no arrow game is over
            if arrowCount == 0:
                print("You're out of arrows! Game over.")
                playerAlive = False

        #if M is inputed movePlayer is called and results are determined
        elif playerIn == "M":
            playerPos = movePlayer(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos)
            if playerPos == 21:
                print("YYYYIIIIEEEE... Fell in pit!")
                print("Ha ha ha - you lose!")
                playerAlive = False
            if playerPos == 22:
                print("You have been eaten by the Wumpus!")
                print("Ha ha ha - you lose!")
                playerAlive = False
        else:
            #This happens if you suck at games
            print("What the sigma!")




main()