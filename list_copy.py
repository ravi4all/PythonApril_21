Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [4,3,5,6,7,3,12]
>>> data_1 = data
>>> data_1 == data
True
>>> data is data_1
True
>>> data_1[0] = 100
>>> data
[100, 3, 5, 6, 7, 3, 12]
>>> data_1
[100, 3, 5, 6, 7, 3, 12]
>>> data_2 = data[:]
>>> data_2
[100, 3, 5, 6, 7, 3, 12]
>>> data
[100, 3, 5, 6, 7, 3, 12]
>>> data == data_2
True
>>> data is data_2
False
>>> data[:]
[100, 3, 5, 6, 7, 3, 12]
>>> data_2 = data[:]
>>> data[0] = 50
>>> data
[50, 3, 5, 6, 7, 3, 12]
>>> data_2
[100, 3, 5, 6, 7, 3, 12]
>>> data = [4,3,65,7,2,3,[1,12,45,67,8]]
>>> data_2 = data[:]
>>> data_2 = data.copy()
>>> data[0] = 100
>>> data
[100, 3, 65, 7, 2, 3, [1, 12, 45, 67, 8]]
>>> data_2
[4, 3, 65, 7, 2, 3, [1, 12, 45, 67, 8]]
>>> data[-1]
[1, 12, 45, 67, 8]
>>> data[-1][0] = 110
>>> data
[100, 3, 65, 7, 2, 3, [110, 12, 45, 67, 8]]
>>> data_2
[4, 3, 65, 7, 2, 3, [110, 12, 45, 67, 8]]
>>> import copy
>>> data_3 = copy.deepcopy(data)
>>> 