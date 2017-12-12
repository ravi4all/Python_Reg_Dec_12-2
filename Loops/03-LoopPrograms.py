# Print Table of any number
'''
a = 5
for i in range(1,11):
    print(a,"x",i, "=", a*i )
'''
##a = int(input("Enter the number : "))
##for i in range(1,11):
##    print(a,"x",i, "=", a*i )

# Nested Loops
for i in range(600):
    for j in range(500):
        print("Inside J Loop",j+1)
        for k in range(400):
            print("Inside K Loop",k+1)
    print("Inside I Loop",i+1)
    print("----------------------------")
