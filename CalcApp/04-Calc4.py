def calculator(x,y,opr):
    return eval(x + opr + y)

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")

    todo = {
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*"
    }

    result = calculator(num_1, num_2, todo.get(userChoice))
    print(result)


