def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    return z1, z2, z3, z4

# packing and unpacking
# print(calc(5,6))
# a = calc(5,6)

# a, b, c, d = calc(5,6)
# print("Sum is",a)

a,b,*c = calc(5,6)
print(a,b,c)
