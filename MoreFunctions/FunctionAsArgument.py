def outer(x):
    print("This is outer function")
    return x
    # x()

@outer
def func_1():
    print("This is some another function")

# y = outer(func_1)
# print(y())

func_1()
