# Dynamic Arguments

# *args and **kwargs

# def emp(name, *address):
#     print("Name : {} and Address : {}".format(name, address))
    # for a in address:
    #     print(a)

# emp("Ram", "xyz")
# emp("Ram", ["xyz", "ijk", "abc"])

# emp("Ram", "xyz", "ijk", "abc")

def emp(**kwargs):
    print(kwargs)

emp(name = "Ram", age = 20, salary = 15000)
