Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> a = b
>>> a
20
>>> b
20
>>> temp = 0
>>> a = 10
>>> a
10
>>> b
20
>>> temp
0
>>> temp = a
>>> a = b
>>> a
20
>>> b = temp
>>> b
10
>>> a = 10
>>> a,b = 10, 20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> 
