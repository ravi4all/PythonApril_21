Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = list()
>>> data = []
>>> data = [1,3,5,7,1,3,5,12,11,6,54,68,'hello', 'hi']
>>> data[0]
1
>>> data[0:5]
[1, 3, 5, 7, 1]
>>> data[5:10]
[3, 5, 12, 11, 6]
>>> data[::-1]
['hi', 'hello', 68, 54, 6, 11, 12, 5, 3, 1, 7, 5, 3, 1]
>>> data = []
>>> data.append(5)
>>> data
[5]
>>> data.append(12)
>>> data.append(1)
>>> data.append(10)
>>> data.append(21)
>>> data
[5, 12, 1, 10, 21]
>>> data.append(2,1,3,5,7,8)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data.append(2,1,3,5,7,8)
TypeError: append() takes exactly one argument (6 given)
>>> data.append([2,1,3,5,7,8])
>>> data
[5, 12, 1, 10, 21, [2, 1, 3, 5, 7, 8]]
>>> data.pop()
[2, 1, 3, 5, 7, 8]
>>> data
[5, 12, 1, 10, 21]
>>> data.pop(2)
1
>>> data
[5, 12, 10, 21]
>>> data.extend([2, 1, 3, 5, 7, 8])
>>> data
[5, 12, 10, 21, 2, 1, 3, 5, 7, 8]
>>> data.insert(2,100)
>>> data
[5, 12, 100, 10, 21, 2, 1, 3, 5, 7, 8]
>>> data.remove(6)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data.remove(6)
ValueError: list.remove(x): x not in list
>>> data.remove(5)
>>> data
[12, 100, 10, 21, 2, 1, 3, 5, 7, 8]
>>> data
[12, 100, 10, 21, 2, 1, 3, 5, 7, 8]
>>> del data[3]
>>> data
[12, 100, 10, 2, 1, 3, 5, 7, 8]
>>> data.count(1)
1
>>> data.count(10)
1
>>> data.reverse()
>>> data
[8, 7, 5, 3, 1, 2, 10, 100, 12]
>>> sorted(data)
[1, 2, 3, 5, 7, 8, 10, 12, 100]
>>> sorted(data,reverse=True)
[100, 12, 10, 8, 7, 5, 3, 2, 1]
>>> data
[8, 7, 5, 3, 1, 2, 10, 100, 12]
>>> data.sort()
>>> data
[1, 2, 3, 5, 7, 8, 10, 12, 100]
>>> data[0] = 100
>>> data
[100, 2, 3, 5, 7, 8, 10, 12, 100]
>>> data[0:3] = [53,7,11]
>>> data
[53, 7, 11, 5, 7, 8, 10, 12, 100]
>>> len(data)
9
>>> for i in range(len(data)):
	print(data[i])

	
53
7
11
5
7
8
10
12
100
>>> for i in range(len(data)):
	print(i, data[i])

	
0 53
1 7
2 11
3 5
4 7
5 8
6 10
7 12
8 100
>>> for item in data:
	print(item)

	
53
7
11
5
7
8
10
12
100
>>> names = ['Ram','Shyam','Gopal','Mohan']
>>> dept = ['IT','HR','IT','IT']
>>> sal = [45000,43000,28000,25000]
>>> data = [names, dept, sal]
>>> data
[['Ram', 'Shyam', 'Gopal', 'Mohan'], ['IT', 'HR', 'IT', 'IT'], [45000, 43000, 28000, 25000]]
>>> data[0]
['Ram', 'Shyam', 'Gopal', 'Mohan']
>>> data[1]
['IT', 'HR', 'IT', 'IT']
>>> data[2]
[45000, 43000, 28000, 25000]
>>> data[0]
['Ram', 'Shyam', 'Gopal', 'Mohan']
>>> data[0][0]
'Ram'
>>> for i in range(len(data)):
	print(data[i])

	
['Ram', 'Shyam', 'Gopal', 'Mohan']
['IT', 'HR', 'IT', 'IT']
[45000, 43000, 28000, 25000]
>>> for i in range(len(data)):
	print(data[i][i])

	
Ram
HR
28000
>>> for i in range(len(data)):
	print(data[0][i], data[1][i], data[2][i])

	
Ram IT 45000
Shyam HR 43000
Gopal IT 28000
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[j][i], end=',')
	print()

	
Ram,IT,45000,Traceback (most recent call last):
  File "<pyshell#75>", line 3, in <module>
    print(data[j][i], end=',')
IndexError: list index out of range
>>> for i in range(len(data[i])):
	for j in range(len(data)):
		print(data[j][i], end=',')
	print()

	
Ram,IT,45000,
Shyam,HR,43000,
Gopal,IT,28000,
Mohan,IT,25000,
>>> data
[['Ram', 'Shyam', 'Gopal', 'Mohan'], ['IT', 'HR', 'IT', 'IT'], [45000, 43000, 28000, 25000]]
>>> data = [['Ram','IT', 45000],['Shyam','HR',35000],['Sam','IT',41000]]
>>> data = []
>>> for i in range(51):
	data.append(i)

	
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> data = []
>>> for i in range(51):
	if i % 2 == 0:
		data.append(i)

		
>>> data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data = [i for i in range(51)]
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> data = [i for i in range(51) if i % 2 == 0]
>>> data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data = [[i,j] for i in range(10) for j in range(5)]
>>> data
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4]]
>>> 