def main():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        result = a + b
        print("Result is",result)
        result = a - b
        print("Result is",result)
        result = a / b
        print("Result is",result)
        result = a * b
        print("Result is",result)

    # except BaseException as err:
    #     print("Error : ",err)
        # print("Some error")

    except (ZeroDivisionError, ValueError, ArithmeticError) as err:
        print(err)
        main()

main()
