def calc(x, y):
    z = x + y
    print("Sum is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

operations = {}

operations.get(ch)(x,y)

operations.get(int(ch))