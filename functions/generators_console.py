Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> def sayHello():
	print("Hello world")
	return
	print("Bye world")

	
>>> sayHello()
Hello world
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> counter()
1
>>> def counter(x):
	while True:
		x += 1
		return x

	
>>> counter(0)
1
>>> counter(1)
2
>>> counter(2)
3
>>> def counter(x):
	x = 0
	while True:
		x += 1
		yield x

		
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter()
<generator object counter at 0x0000026047283F90>
>>> for i in range(1,10):
	print(i, end=',')

	
1,2,3,4,5,6,7,8,9,
>>> range
<class 'range'>
>>> next(counter())
1
>>> next(counter())
1
>>> next(counter())
1
>>> view = counter()
>>> next(view)
1
>>> next(view)
2
>>> next(view)
3
>>> next(view)
4
>>> next(view)
5
>>> next(view)
6
>>> for i in counter():
	print(i)
	if i == 20:
		break

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> for i in view:
	print(i)
	if i == 20:
		break

	
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> [i for i in range(1,11)]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> (i for i in range(1,11))
<generator object <genexpr> at 0x0000026047283F90>
>>> x = (i for i in range(1,11))
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> next(x)
4
>>> 