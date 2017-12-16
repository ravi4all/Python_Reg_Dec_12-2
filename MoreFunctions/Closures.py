def parent(x):

    def child():
        print("Inside Child")
        return x + 1

    # print(child())
    return child

a = parent(12)
print(a())
