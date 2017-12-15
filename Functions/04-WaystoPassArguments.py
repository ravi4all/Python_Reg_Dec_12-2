# def emp(name, age):
#     print("Name : {} and Age : {}".format(name, age))

def emp(name = None, age = 0):
    print("Name : {} and Age : {}".format(name, age))


# Normal Arguments
emp("Ram", 20)

# Default Arguments
emp()

# Initialize Arguments
emp(name = 'Shyam', age = 23)
