Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {}
>>> type(data)
<class 'dict'>
>>> data = {'id':101,'name':'John','dept':'IT'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['id']
101
>>> data['name']
'John'
>>> data['dept']
'IT'
>>> data.keys()
dict_keys(['id', 'name', 'dept'])
>>> data.values()
dict_values([101, 'John', 'IT'])
>>> data.items()
dict_items([('id', 101), ('name', 'John'), ('dept', 'IT')])
>>> data['salary']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data['salary']
KeyError: 'salary'
>>> data.get('id')
101
>>> data.get('salary')
>>> data.get('salary','Data Not available')
'Data Not available'
>>> data
{'id': 101, 'name': 'John', 'dept': 'IT'}
>>> data.get('name','Data Not available')
'John'
>>> data['salary'] = 45000
>>> data
{'id': 101, 'name': 'John', 'dept': 'IT', 'salary': 45000}
>>> data['address'] = 'Delhi'
>>> data
{'id': 101, 'name': 'John', 'dept': 'IT', 'salary': 45000, 'address': 'Delhi'}
>>> data.popitem()
('address', 'Delhi')
>>> data.pop('dept')
'IT'
>>> data
{'id': 101, 'name': 'John', 'salary': 45000}
>>> data.setdefault('dept')
>>> data
{'id': 101, 'name': 'John', 'salary': 45000, 'dept': None}
>>> data['dept'] = 'IT'
>>> data
{'id': 101, 'name': 'John', 'salary': 45000, 'dept': 'IT'}
>>> data.setdefault('address','Delhi')
'Delhi'
>>> data
{'id': 101, 'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> details = {'company':'TCS','bank':}
SyntaxError: invalid syntax
>>> 
>>> details = {'company':'TCS','bank':'HDFC'}
>>> data + details
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    data + details
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> data.update(details)
>>> data
{'id': 101, 'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi', 'company': 'TCS', 'bank': 'HDFC'}
>>> data['bank'] = 'ICICI'
>>> data
{'id': 101, 'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi', 'company': 'TCS', 'bank': 'ICICI'}
>>> for item in data:
	print(item)

	
id
name
salary
dept
address
company
bank
>>> for item in data:
	print(data[item])

	
101
John
45000
IT
Delhi
TCS
ICICI
>>> for item in data:
	print(item, data[item])

	
id 101
name John
salary 45000
dept IT
address Delhi
company TCS
bank ICICI
>>> for item in data:
	print(item, ":", data[item])

	
id : 101
name : John
salary : 45000
dept : IT
address : Delhi
company : TCS
bank : ICICI
>>> for item in data.values():
	print(item)

	
101
John
45000
IT
Delhi
TCS
ICICI
>>> 