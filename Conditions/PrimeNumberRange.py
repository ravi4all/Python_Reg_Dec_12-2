min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

for num in range(min_range, max_range):
    for i in range(2,num):
        if num % i == 0:
            print("{} is Not Prime".format(num))
            break
    else:
        print("{} is Prime".format(num))
