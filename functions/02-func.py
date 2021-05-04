#Scope of variables : local and global

# global variable
x = 10
y = 20

def add():
    # local variables
    x = 56
    y = 6
    z = x + y
    print("Sum is",z)

add()
print(f"x is {x} and y is {y}")
