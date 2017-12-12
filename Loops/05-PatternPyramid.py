'''
      *
     ***
    *****
   *******
  *********
'''

for i in range(1,6):
    for j in reversed(range(1,6-i)):
        print(" ",end='')
    for k in range(2*i-1):
        print('*', end='')
    print()

# Alternative
for i in range(1,6):
    print(' ' * (6-i) + '*' * (2*i-1))
