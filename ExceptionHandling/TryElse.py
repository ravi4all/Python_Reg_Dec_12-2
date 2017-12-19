try:
    a = 12
    b = 5
    c = a/b
    print("Result is",c)

except BaseException as err:
    print(err)

else:
    print("Inside Else block")
