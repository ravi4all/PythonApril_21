'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print('#' * 50)

'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print('#' * 50)

'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()

print('#' * 50)

'''
1
23
456
78910
'''
k = 0
for i in range(1,5):
    for j in range(1,i+1):
        #k += 1
        k = k + 1
        print(k, end='')
    print()

print('#' * 50)


'''
	*
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
'''
for i in range(10):
    for j in range(10-i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()






