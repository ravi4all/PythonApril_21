Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> type(x)
<class 'int'>
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = (10,)
>>> type(x)
<class 'tuple'>
>>> x = (10,12,12,45,67,34,5,7,8)
>>> x
(10, 12, 12, 45, 67, 34, 5, 7, 8)
>>> x = 10,12,12,45,67,34,5,7,8
>>> type(x)
<class 'tuple'>
>>> x[0]
10
>>> x[0:10]
(10, 12, 12, 45, 67, 34, 5, 7, 8)
>>> x[0:4]
(10, 12, 12, 45)
>>> x[0:8:2]
(10, 12, 67, 5)
>>> x.count(12)
2
>>> x.index(5)
6
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name, age, sal = 'Ram', 45, 45000
>>> data
('Ram', 45, 45000)
>>> name
'Ram'
>>> age
45
>>> sal
45000
>>> data = ([2,3,54,5],[1,2,5,6],(1,4,5,7))
>>> data
([2, 3, 54, 5], [1, 2, 5, 6], (1, 4, 5, 7))
>>> 