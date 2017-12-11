Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.forward(200)
>>> t.up(90)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.up(90)
TypeError: penup() takes 1 positional argument but 2 were given
>>> t.up()
>>> t.forward()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t.forward()
TypeError: forward() missing 1 required positional argument: 'distance'
>>> t.forward(200)
>>> t.reset()
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.reset()
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Dec_2017/Regular/Python_12-2/CorePython/Loops/01-SimpleForLoop.py 
0
Hello
Bye
1
Hello
Bye
2
Hello
Bye
3
Hello
Bye
4
Hello
Bye
5
Hello
Bye
6
Hello
Bye
7
Hello
Bye
8
Hello
Bye
9
Hello
Bye
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Dec_2017/Regular/Python_12-2/CorePython/Loops/01-SimpleForLoop.py 
0
Hello
1
Hello
2
Hello
3
Hello
4
Hello
5
Hello
6
Hello
7
Hello
8
Hello
9
Hello
Bye
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Dec_2017/Regular/Python_12-2/CorePython/Loops/01-SimpleForLoop.py 
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
Hello
Bye
>>> import turtle
>>> turtle.Pen()
<turtle.Turtle object at 0x000001DBB14847F0>
>>> for i in range(1,5):
	turtle.forward(200)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.forward(5 * i)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(40):
	turtle.forward(8 * i)
	turtle.left(45)

	
>>> turtle.reset()
>>> for i in range(40):
	turtle.circle(20)
	turtle.left(20)

	
>>> turtle.reset()
>>> for i in range(40):
	turtle.circle(6 * i)
	turtle.left(20)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    turtle.circle(6 * i)
  File "<string>", line 8, in circle
  File "C:\Python36\lib\turtle.py", line 1992, in circle
    self.speed(0)
  File "C:\Python36\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(40):
	turtle.circle(6 * i)
	turtle.left(20)

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> turtle.shape('turtle')
>>> for i in range(40):
	turtle.circle(6 * i)
	turtle.left(5*i)

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> while True:
	for i in range(40):
		turtle.circle(6 * i)
		turtle.left(20)
	turtle.reset()
	turtle.speed(0)

	
Traceback (most recent call last):
  File "<pyshell#51>", line 3, in <module>
    turtle.circle(6 * i)
  File "<string>", line 8, in circle
  File "C:\Python36\lib\turtle.py", line 1997, in circle
    self.speed(speed)
  File "C:\Python36\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> 
