Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = {2,1,4,4,5,7}
>>> y = {2,34,56,8,9,5,4,2,6,9,0,4}
>>> x
{1, 2, 4, 5, 7}
>>> y
{0, 2, 34, 4, 5, 6, 8, 9, 56}
>>> x.intersection(y)
{2, 4, 5}
>>> x & y
{2, 4, 5}
>>> x.union(y)
{0, 1, 2, 34, 4, 5, 6, 7, 8, 9, 56}
>>> x | y
{0, 1, 2, 34, 4, 5, 6, 7, 8, 9, 56}
>>> x.difference(y)
{1, 7}
>>> x - y
{1, 7}
>>> y - x
{0, 34, 6, 8, 9, 56}
>>> 