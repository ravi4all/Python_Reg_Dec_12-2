Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> even = []
>>> for i in range(101):
	if i % 2 == 0:
		even.append(i)

>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> even = [i for i in range(101)]
>>> even
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> even = [i for i in range(101) if i % 2 == 0]
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> import time
>>> for i in range(10):
	print(i)
	time.sleep(1)

	
0
1
2
3
4
5
6
7
8
9
>>> import datetime
>>> now = datetime.datetime.now
>>> now
<built-in method now of type object at 0x0000000059FB8510>
>>> today = datetime.datetime.now()
>>> today
datetime.datetime(2017, 12, 17, 13, 8, 20, 165261)
>>> print(today)
2017-12-17 13:08:20.165261
>>> import calendar
>>> cal = calendar.month(2017,12)
>>> print(cal)
   December 2017
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

>>> calendar.calendar
<bound method TextCalendar.formatyear of <calendar.TextCalendar object at 0x000002B9F3DF0B00>>
>>> calendar.calendar(2017)
'                                  2017\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n                   1             1  2  3  4  5             1  2  3  4  5\n 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12\n 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19\n16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26\n23 24 25 26 27 28 29      27 28                     27 28 29 30 31\n30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n                1  2       1  2  3  4  5  6  7                1  2  3  4\n 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11\n10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18\n17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25\n24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n                1  2          1  2  3  4  5  6                   1  2  3\n 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10\n10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17\n17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24\n24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30\n31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n                   1             1  2  3  4  5                   1  2  3\n 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10\n 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17\n16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24\n23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31\n30 31\n'
>>> cal = calendar.calendar(2017)
>>> print(cal)
                                  2017

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31

>>> a = {"id" : 101, "Name" : "Ram"}
>>> a
{'id': 101, 'Name': 'Ram'}
>>> list(a)
['id', 'Name']
>>> a
{'id': 101, 'Name': 'Ram'}
>>> a = {"id" : 101, "Name" : "Ram", "Age" : 23, "Salary" : 15000}
>>> list_1 = list(a)
>>> list_1
['id', 'Name', 'Age', 'Salary']
>>> list_2 = list(a.values())
>>> list_2
[101, 'Ram', 23, 15000]
>>> for i,j in ziplist_1, list_2
SyntaxError: invalid syntax
>>> zip(list_1, list_2)
<zip object at 0x000002B9F3E00B48>
>>> list(zip(list_1, list_2))
[('id', 101), ('Name', 'Ram'), ('Age', 23), ('Salary', 15000)]
>>> for i in zip(list_1, list_2):
	print(i)

	
('id', 101)
('Name', 'Ram')
('Age', 23)
('Salary', 15000)
>>> for i in enumerate(range(10)):
	print(i)

	
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 5)
(6, 6)
(7, 7)
(8, 8)
(9, 9)
>>> for i in enumerate(range(10,20)):
	print(i)

	
(0, 10)
(1, 11)
(2, 12)
(3, 13)
(4, 14)
(5, 15)
(6, 16)
(7, 17)
(8, 18)
(9, 19)
>>> for i,j in enumerate(range(10,20)):
	print(i,j)

	
0 10
1 11
2 12
3 13
4 14
5 15
6 16
7 17
8 18
9 19
>>> 
