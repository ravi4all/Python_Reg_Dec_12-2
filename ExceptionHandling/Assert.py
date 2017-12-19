def calc(x,y):
    c = 0
    # Assert - Debugging...It is like if condition
    try:
        assert (x > y), "First value should be greater"
        c = x - y
        print("Value of c",c)
    except AssertionError as err:
        print(err)

calc(10,50)
