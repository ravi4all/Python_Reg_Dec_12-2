Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.system('calculator')
1
>>> os.open('music_1.ogg')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.open('music_1.ogg')
TypeError: Required argument 'flags' (pos 2) not found
>>> os.system('music_1.ogg')
0
>>> os.getcwd()
'C:\\Python36'
>>> os.system('dhoni.mp4')
0
>>> import sys
>>> os.open('calculator')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.open('calculator')
TypeError: Required argument 'flags' (pos 2) not found
>>> os.startfile('calculator')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    os.startfile('calculator')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'calculator'
>>> os.startfile('calc')
>>> os.startfile('notepad')
>>> os.chdir('C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Dec_2017\Regular\Python_12-2\CorePython\Modules')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.getcwd()
'C:\\Python36'
>>> print("Hello\nWorld")
Hello
World
>>> print(r"Hello\nWorld")
Hello\nWorld
>>> os.chdir(r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Dec_2017\Regular\Python_12-2\CorePython\Modules')
>>> os.getcwd()
'C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\Dec_2017\\Regular\\Python_12-2\\CorePython\\Modules'
>>> import math
>>> math.floor(2.6)
2
>>> math.floor(2.2)
2
>>> math.ceil(2.2)
3
>>> math.ceil(2.5)
3
>>> math.pow(12,4)
20736.0
>>> math.pow(2,4)
16.0
>>> math.sqrt(56)
7.483314773547883
>>> math.cos(10)
-0.8390715290764524
>>> math.cos(0)
1.0
>>> math.cos(30)
0.15425144988758405
>>> math.cos(90)
-0.4480736161291701
>>> math.sin(90)
0.8939966636005579
>>> math.sin(0)
0.0
>>> import statistics
>>> data = [12,34,4,67,34,22,54,7,8,9,11]
>>> statistics.mean(data)
23.818181818181817
>>> statistics.median(data)
12
>>> statistics.stdev(data)
21.060950509500667
>>> 
