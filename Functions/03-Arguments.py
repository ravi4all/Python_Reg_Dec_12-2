# Arguments - the value or variable that we pass inslide (...)

def add(x,y):
    print(x + y)

def sub(x,y):
    print(x - y)

def div(x,y):
    # print(x/y)
    print(x/y if x > y else y/x)

def mul(x,y):
    print(x*y)

add(10,11)
sub(23,10)
div(5,25)
mul(25,5)
