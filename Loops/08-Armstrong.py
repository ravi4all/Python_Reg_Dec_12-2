a = 153
temp = a
s = 0

while a > 0:
    r = a % 10
    s = r**3 + s
    a = a//10
    print("Current Value of a is",a)
    print("Current Value of s is",s)
