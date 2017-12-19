def calc(x,y):
    c = 0
    try:
        if x < y:
            raise ValueError("First Value must be greater")
        else:
            c = x - y
            print("Value of c",c)
    except ValueError as err:
        print(err)

calc(10,50)
