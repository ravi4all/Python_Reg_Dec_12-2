Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = {1,2,3,4,5,6,7}
>>> type(s)
<class 'set'>
>>> s1 = {5,4,8,9,2,0,11}
>>> s.intersection(s1)
{2, 4, 5}
>>> s.union(s1)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
>>> a = [1,2,3,4,6,7,2,3,7,1,5]
>>> type(a)
<class 'list'>
>>> set(a)
{1, 2, 3, 4, 5, 6, 7}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> 
