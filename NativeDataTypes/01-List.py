Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,45,'Hello', 10.5, 'Bye']
>>> a[0]
12
>>> a[-1]
'Bye'
>>> a[0:4]
[12, 45, 'Hello', 10.5]
>>> a[0] = "Hey"
>>> a
['Hey', 45, 'Hello', 10.5, 'Bye']
>>> a = []
>>> a.append(5)
>>> a
[5]
>>> a.append(10)
>>> a
[5, 10]
>>> b = [12, 45, 'Hello', 10.5]
>>> b.append('Bye')
>>> b
[12, 45, 'Hello', 10.5, 'Bye']
>>> a
[5, 10]
>>> a.append(15)
>>> a
[5, 10, 15]
>>> a.append(15,20,25,30)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append(15,20,25,30)
TypeError: append() takes exactly one argument (4 given)
>>> a.append([15,20,25,30])
>>> a
[5, 10, 15, [15, 20, 25, 30]]
>>> a[3]
[15, 20, 25, 30]
>>> a[3][0]
15
>>> a
[5, 10, 15, [15, 20, 25, 30]]
>>> a.pop()
[15, 20, 25, 30]
>>> a
[5, 10, 15]
>>> a.extend([20,25,30])
>>> a
[5, 10, 15, 20, 25, 30]
>>> a.insert(0, 0)
>>> a
[0, 5, 10, 15, 20, 25, 30]
>>> a.pop(3)
15
>>> a
[0, 5, 10, 20, 25, 30]
>>> a.index(10)
2
>>> a.remove(10)
>>> a
[0, 5, 20, 25, 30]
>>> a.remove(100)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.remove(100)
ValueError: list.remove(x): x not in list
>>> a.extend([12,18,6,3,19])
>>> a
[0, 5, 20, 25, 30, 12, 18, 6, 3, 19]
>>> 30 in a
True
>>> 31 in a
False
>>> a.sort()
>>> a
[0, 3, 5, 6, 12, 18, 19, 20, 25, 30]
>>> a.sort(reverse = True)
>>> a
[30, 25, 20, 19, 18, 12, 6, 5, 3, 0]
>>> a.clear()
>>> a
[]
>>> 
