Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 'hello'
>>> import turtle
>>> t = turtle.Pen()
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> t.shape('turtle')
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(30):
	t.forward(5 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(30):
	t.forward(5 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(30):
	print(i,5 * i)
	t.forward(5 * i)
	t.left(45)

	
0 0
1 5
2 10
3 15
4 20
5 25
6 30
7 35
8 40
9 45
10 50
11 55
12 60
13 65
14 70
15 75
16 80
17 85
18 90
19 95
20 100
21 105
22 110
23 115
24 120
25 125
26 130
27 135
28 140
29 145
>>> t.reset()
>>> for i in range(30):
	t.circle(5 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(5):
	print(i * 2)

	
0
2
4
6
8
>>> for i in range(1,11):
	print(i * 2)

	
2
4
6
8
10
12
14
16
18
20
>>> 
============ RESTART: F:/Batches/April/PythonEve/table_program.py ============
Enter the number : 45
45 x 1 = 45
45 x 2 = 90
45 x 3 = 135
45 x 4 = 180
45 x 5 = 225
45 x 6 = 270
45 x 7 = 315
45 x 8 = 360
45 x 9 = 405
45 x 10 = 450
>>> 