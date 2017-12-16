def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def mul(x,y):
    return x * y

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
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
    }

    result = todo.get(userChoice)(num_1, num_2)
    print("Result is",result)
