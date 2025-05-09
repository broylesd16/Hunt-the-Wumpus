import random

def movePlayer(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos):
    moveInput = int(input("Where to?"))
    while moveInput not in wumpusMap[playerPos]:
        moveInput = int(input("Not possible - Where to?"))

    if moveInput == bat1Pos or moveInput == bat2Pos:
        moveInput = batLogic()
        while moveInput == bat1Pos or moveInput == bat2Pos:
            moveInput = batLogic()
    elif moveInput == hole1Pos or moveInput == hole2Pos:
        moveInput = 21
    elif moveInput == wumpusPos:
        moveInput = 22


    return moveInput

def batLogic():
    print("ZAP--Super Bat snatch! Elsewhereville for you!")
    return random.randint(1,20)

def checkHazards(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos):
    warnings = ""

    if wumpusPos in wumpusMap[playerPos]:
        warnings = warnings + "You smell a wumpus" + "\n"

    if bat1Pos in wumpusMap[playerPos] or bat2Pos in wumpusMap[playerPos]:
        warnings = warnings + "You hear flapping" + "\n"

    if hole1Pos in wumpusMap[playerPos] or hole2Pos in wumpusMap[playerPos]:
        warnings = warnings + "You feel a draft" + "\n"

    return warnings

def shootArrow():
    print("F")

def main():
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

    print(playerPos, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos)

    print("Welcome to Hunt the Wumpus")

    playerAlive = True
    while playerAlive == True:
        print(f"You are in room {playerPos}")
        print(f"Tunnels lead to {wumpusMap[playerPos]}")
        print(checkHazards(playerPos, wumpusMap, bat1Pos, bat2Pos, hole1Pos, hole2Pos, wumpusPos))
        playerIn = input("Shoot, Move or Quit (S-M-Q)?")
        if playerIn == "Q":
            playerAlive = False
            print("Chicken!")
        elif playerIn == "S":
            shootArrow()
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
            print("What the sigma!")




main()