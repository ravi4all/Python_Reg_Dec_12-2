import random

cpu_dict = ["Hi", "Hello", "Hey", "Good morning", "Bye", "Have a nice day", "See you"]

while True:
    
    userMessage = input("Enter your message : ")

    cpuMessage = random.choice(cpu_dict)

    print(cpuMessage)
