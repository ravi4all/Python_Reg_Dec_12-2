import random
shoot = 0

while True:
    myX = random.randint(0,10)
    zombieX = random.randint(0,10)
    if myX == zombieX:
        print("Match Found")
        shoot += 1
        if shoot == 3:
            print("Zombie Killed...")
            break
    print(shoot)
