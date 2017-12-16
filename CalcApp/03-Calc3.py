def calculator(x,y,ch):
    if ch == "1":
        return x + y
    elif ch == "2":
        return x - y
    elif ch == "3":
        return x / y
    elif ch == "4":
        return x * y
    else:
        return "Wrong Choice"

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    todo = {
        "1" : calculator,
        "2" : calculator,
        "3" : calculator,
        "4" : calculator
    }

    result = todo.get(userChoice)(num_1, num_2, userChoice)
    print("Result is",result)
