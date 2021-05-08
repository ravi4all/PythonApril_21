def add(*x):
    # print(x)
    s = 0
    for i in range(len(x)):
        s += x[i]
    print("Sum is",s)

add(3,4)
add(4,3,5,6)
add(3,4,6,8,84)
