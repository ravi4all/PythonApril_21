#Build a calculator
'''
1. Take 2 numbers from user as input
2. Print menu in front of user
   a. Press 1 for Addition
   b. Press 2 for Subtraction
   c. Press 3 for Multiplication
   d. Press 4 for division
3. Ask user's choice that which operation user want to perform
4. Perform that particular operation on those two numbers
'''
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

if ch == "1":
    result = num_1 + num_2
    print("Sum is",result)






