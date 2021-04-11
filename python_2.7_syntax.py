Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> print "Hello World"
Hello World
>>> a = 5
>>> b = 6
>>> c = a + b
>>> print("Sum is",c)
('Sum is', 11)
>>> print "Sum is",c
Sum is 11
>>> input("Enter your name : ")
Enter your name : Ram

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    input("Enter your name : ")
  File "<string>", line 1, in <module>
NameError: name 'Ram' is not defined
>>> age - input("Enter your age ")

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    age - input("Enter your age ")
NameError: name 'age' is not defined
>>> 
>>> age = input("Enter your age ")
Enter your age 65
>>> age
65
>>> type(age)
<type 'int'>
>>> age = raw_input("Enter your name : ")
Enter your name : Ram
>>> game = True
>>> True = False
>>> game = True
>>> game
False
>>> import keyword
>>> keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
31
>>> 
