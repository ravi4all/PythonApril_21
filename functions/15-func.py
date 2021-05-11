def even(n):
    return n % 2 == 0

# print(even(7))
numbers = [2,5,7,8,8,4,1,12,34,67,8,2]
print(list(filter(even, numbers)))