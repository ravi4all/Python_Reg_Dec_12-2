Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 20
>>> b = 12
>>> c = a > b
>>> c
True
>>> c = a < b
>>> 
>>> c
False
>>> a is b
False
>>> a is not b
True
>>> a = b
>>> a is b
True
>>> a = 10
>>> b = 12
>>> b = 10
>>> a
10
>>> b
10
>>> a is b
True
>>> list_1 = [12,13,14,151,61,23]
>>> list_2 = list_1
>>> list_2
[12, 13, 14, 151, 61, 23]
>>> list_1 is list_2
True
>>> list_1[0] = "Hello"
>>> list_1
['Hello', 13, 14, 151, 61, 23]
>>> list_2
['Hello', 13, 14, 151, 61, 23]
>>> a = 10
>>> b = 12
>>> id(a)
1509738448
>>> id(b)
1509738512
>>> a = b
>>> id(a)
1509738512
>>> id(b)
1509738512
>>> a
12
>>> b
12
>>> a = 13
>>> a
13
>>> b
12
>>> id(a)
1509738544
>>> id(b)
1509738512
>>> list_1
['Hello', 13, 14, 151, 61, 23]
>>> list_2
['Hello', 13, 14, 151, 61, 23]
>>> list_3 =
SyntaxError: invalid syntax
>>> list_3 = list_1[:]
>>> list_3
['Hello', 13, 14, 151, 61, 23]
>>> list_1
['Hello', 13, 14, 151, 61, 23]
>>> list_1 is list_3
False
>>> id(list_1)
2753438775368
>>> id(list_2)
2753438775368
>>> id(list_3)
2753438775688
>>> list_1[1] = "Bye"
>>> list_1
['Hello', 'Bye', 14, 151, 61, 23]
>>> list_3
['Hello', 13, 14, 151, 61, 23]
>>> list_1 = ['Hello', 'Bye', 14, [151, 61, 23], 10.5, 12.5]
>>> list_1
['Hello', 'Bye', 14, [151, 61, 23], 10.5, 12.5]
>>> list_3 = list_1[:]
>>> list_1[0] = 0
>>> list_1
[0, 'Bye', 14, [151, 61, 23], 10.5, 12.5]
>>> list_3
['Hello', 'Bye', 14, [151, 61, 23], 10.5, 12.5]
>>> list_1[3][0] = "Hello"
>>> list_1
[0, 'Bye', 14, ['Hello', 61, 23], 10.5, 12.5]
>>> list_3
['Hello', 'Bye', 14, ['Hello', 61, 23], 10.5, 12.5]
>>> import copy
>>> list_3 = copy.deepcopy(list_1)
>>> list_3
[0, 'Bye', 14, ['Hello', 61, 23], 10.5, 12.5]
>>> list_1
[0, 'Bye', 14, ['Hello', 61, 23], 10.5, 12.5]
>>> list_1[3][0] = "Python"
>>> list_1
[0, 'Bye', 14, ['Python', 61, 23], 10.5, 12.5]
>>> list_3
[0, 'Bye', 14, ['Hello', 61, 23], 10.5, 12.5]
>>> 
