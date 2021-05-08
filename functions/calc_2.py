def add(x, y):
    z = x + y
    print("Sum is",z)

def sub(x, y):
    z = x - y
    print("Sub is",z)

def div(x, y):
    z = x / y
    print("Div is",z)

def mul(x, y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

operations = [add, sub, div, mul]
operations[int(ch) - 1](x,y)