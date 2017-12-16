def even(num):
    return num % 2 == 0

a = [1,2,3,4,5,6,7,8,9,10]

# ev = list(map(even, a))
# print(ev)

ev = list(filter(even, a))
print(ev)
