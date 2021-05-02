Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [4,5,6,3,6,8,9,23,56,33]
>>> sorted(x)
[3, 4, 5, 6, 6, 8, 9, 23, 33, 56]
>>> sorted(x, reverse=True)
[56, 33, 23, 9, 8, 6, 6, 5, 4, 3]
>>> x = [['John',45],['Sam',42],['Aman',23],['Tom',56]]
>>> sorted(x)
[['Aman', 23], ['John', 45], ['Sam', 42], ['Tom', 56]]
>>> sorted(x, key=1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sorted(x, key=1)
TypeError: 'int' object is not callable
>>> def sort_data(data):
	return data[1]

>>> sorted(x, key=sort_data)
[['Aman', 23], ['Sam', 42], ['John', 45], ['Tom', 56]]
>>> for item in x:
	print(item[1])

	
45
42
23
56
>>> data = [{'name':'John','age':34},{'name':'Mac','age':24},{'name':'Tom','age':74},{'name':'Sam','age':39}]
>>> sorted(data)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sorted(data)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> sorted(data, key=data.get('name'))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sorted(data, key=data.get('name'))
AttributeError: 'list' object has no attribute 'get'
>>> def sort_data(data):
	return data['name']

>>> sorted(data, key=sort_data)
[{'name': 'John', 'age': 34}, {'name': 'Mac', 'age': 24}, {'name': 'Sam', 'age': 39}, {'name': 'Tom', 'age': 74}]
>>> def sort_data(data):
	return data['age']

>>> sorted(data, key=sort_data)
[{'name': 'Mac', 'age': 24}, {'name': 'John', 'age': 34}, {'name': 'Sam', 'age': 39}, {'name': 'Tom', 'age': 74}]
>>> 