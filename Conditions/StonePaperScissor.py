import random

cpu = ["stone", "paper", "scissor"]

userCounter = 0
cpuCounter = 0

game = True

while game:
    userChoice = input("Enter your choice : ")
    cpuChoice = random.choice(cpu)

    if userChoice == cpuChoice:
        print("CPU : ",cpuChoice)
        print("Match Tie")
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    elif userChoice == "stone" and cpuChoice == "scissor":
        print("CPU : ",cpuChoice)
        print("You win")
        userCounter += 1
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    elif userChoice == "paper" and cpuChoice == "stone":
        print("CPU : ",cpuChoice)
        print("You win")
        userCounter += 1
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    elif userChoice == "scissor" and cpuChoice == "paper":
        print("CPU : ",cpuChoice)
        print("You Win")
        userCounter += 1
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    elif userChoice == "stone" and cpuChoice == "paper":
        print("CPU : ",cpuChoice)
        print("CPU win")
        cpuCounter += 1
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    elif userChoice == "paper" and cpuChoice == "scissor":
        print("CPU : ",cpuChoice)
        print("CPU win")
        cpuCounter += 1
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    elif userChoice == "scissor" and cpuChoice == "stone":
        print("CPU : ",cpuChoice)
        print("CPU Win")
        cpuCounter += 1
        print("CPU : {} User : {}".format(cpuCounter, userCounter))

    else:
        print("Wrong Choice")


    if cpuCounter == 5:
        print("CPU Win")
        print("Game Over")
##        game = False
        break
    elif userCounter == 5:
        print("You Win")
        print("Game Over")
##        game = False
        break
    
