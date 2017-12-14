Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = (5,10,15,'hi', 10.5, 100)
>>> a[0]
5
>>> a[-1]
100
>>> a[0:4]
(5, 10, 15, 'hi')
>>> a.index(5)
0
>>> a[0] = "Bye"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[0] = "Bye"
TypeError: 'tuple' object does not support item assignment
>>> a
(5, 10, 15, 'hi', 10.5, 100)
>>> for i in a:
	print(i)

	
5
10
15
hi
10.5
100
>>> 
