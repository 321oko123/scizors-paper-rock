import time
import random
points = 0
pointsAi = 0
round = 0
player = ""
AI = 0
AIdecision = ""
print("play with me rock-paper-scizors. you start")
while True:
    player = input("-")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    AI = random.randint(0, 3)
    if AI == 0:
        AIdecision = "rock"
    elif AI == 1:
        AIdecision = "paper"
    else:
        AIdecision = "scizors"
    if player == AIdecision:
        print(AIdecision)
        print("remis!")
    else:
        if AI == 0 and player == "paper":
            print(AIdecision)
            print("you win")
            points = points + 1
        elif AI == 1 and player == "scizors":
            print(AIdecision)
            print("you win")
            points = points + 1
        elif AI == 2 and player == "rock":
            print(AIdecision)
            print("you win")
            points = points + 1
        else:
            pointsAi = pointsAi + 1
            print(AIdecision)
            print("you lose")
    round = round + 1
    print("round: " + str(round) + "| your points: " + str(points) + "| AI points: " + str(pointsAi) + "| remis: " + str(round - points - pointsAi))