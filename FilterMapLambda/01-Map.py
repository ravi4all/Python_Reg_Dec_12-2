def temp_conv(cel):
    return 9/5 * cel + 32

temp = [32.3,34.5,36.5,31.2,33.6]

# for i in temp:
#     print(temp_conv(i))

f = list(map(temp_conv, temp))
print(f)
