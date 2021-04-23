Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = ""
>>> text = str()
>>> text = "h"
>>> text = "hello"
>>> text = "hello world, this is python programming"
>>> text[0]
'h'
>>> text[10]
'd'
>>> text[23]
't'
>>> len(text)
39
>>> text[38]
'g'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text
'hello world, this is python programming'
>>> text[0:4]
'hell'
>>> text[10:30]
'd, this is python pr'
>>> text[0:10:1]
'hello worl'
>>> #text[start(index/upperbound):stop(position/lowerbound):stop(default=1)]
>>> text[0:20:2]
'hlowrd hsi'
>>> text[10:0]
''
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[:5]
'hello'
>>> text[10:]
'd, this is python programming'
>>> text[:]
'hello world, this is python programming'
>>> text[::-1]
'gnimmargorp nohtyp si siht ,dlrow olleh'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.islower()
True
>>> text.isupper()
False
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text
'hello world, this is python programming'
>>> text.swapcase()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text = text.title()
>>> text
'Hello World, This Is Python Programming'
>>> text.swapcase()
'hELLO wORLD, tHIS iS pYTHON pROGRAMMING'
>>> text.count('i')
2
>>> text.count('o')
4
>>> text.count('o',6)
3
>>> text.count('o',6,20)
1
>>> text.index('o')
4
>>> text.index('i')
15
>>> text.index('p')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    text.index('p')
ValueError: substring not found
>>> text.index('P')
21
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.index('o',31)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    text.index('o',31)
ValueError: substring not found
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',26)
30
>>> text.find('o',31)
-1
>>> text.find('z')
-1
>>> text.rfind('o')
30
>>> text.rfind('o',29)
30
>>> text.rfind('o',20)
30
>>> text.rfind('o',31)
-1
>>> text.rfind('o',0)
30
>>> text.rfind('o',0,5)
4
>>> text.rfind('o',10,20)
-1
>>> text.rfind('o',10,30)
25
>>> text.find('o', 5,30)
7
>>> text.rfind('o',5,30)
25
>>> text
'Hello World, This Is Python Programming'
>>> text.replace('i','x')
'Hello World, Thxs Is Python Programmxng'
>>> text.replace('o','x')
'Hellx Wxrld, This Is Pythxn Prxgramming'
>>> text
'Hello World, This Is Python Programming'
>>> text.split()
['Hello', 'World,', 'This', 'Is', 'Python', 'Programming']
>>> text.split(',')
['Hello World', ' This Is Python Programming']
>>> text = '     Hello World, This Is Python Programming     '
>>> text.strip()
'Hello World, This Is Python Programming'
>>> text.lstrip()
'Hello World, This Is Python Programming     '
>>> text.rstrip()
'     Hello World, This Is Python Programming'
>>> text = text.strip()
>>> text
'Hello World, This Is Python Programming'
>>> text = '######Hello World, This Is Python Programming$$$$$'
>>> text.strip()
'######Hello World, This Is Python Programming$$$$$'
>>> text.strip('$')
'######Hello World, This Is Python Programming'
>>> text = text.strip('$')
>>> text
'######Hello World, This Is Python Programming'
>>> text = text.lstrip('#')
>>> text
'Hello World, This Is Python Programming'
>>> len(text)
39
>>> text.center(4)
'Hello World, This Is Python Programming'
>>> text.center(20)
'Hello World, This Is Python Programming'
>>> text.center(40)
'Hello World, This Is Python Programming '
>>> text.center(41)
' Hello World, This Is Python Programming '
>>> text.center(51)
'      Hello World, This Is Python Programming      '
>>> text.center(51, '#')
'######Hello World, This Is Python Programming######'
>>> text.endswith('?')
False
>>> text.endswith('.')
False
>>> text.endswith('!')
False
>>> text
'Hello World, This Is Python Programming'
>>> text.endswith('g')
True
>>> text.startswith('I')
False
>>> text.startswith('T')
False
>>> text.startswith('H')
True
>>> text.startswith('H',5)
False
>>> text.startswith('W',5)
False
>>> text.startswith('W',6)
True
>>> text.startswith('w',6)
False
>>> text = text.lower()
>>> text.startswith('w',6)
True
>>> 'h' in text
True
>>> 'h' not in text
False
>>> 