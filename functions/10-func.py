# Nested Function
def calc():
    x = 6
    y = 10
    def add():
        z = x + y
        print("Sum is",z)
    def sub():
        z = x - y
        print("Sub is",z)

    return add, sub

operations = calc()
# print(operations)
operations[0]()
operations[1]()