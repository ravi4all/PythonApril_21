# by default input returns string type of data
#name = input("Enter your name : ")
print("Hello",name := input("Enter your name : "))

# so we need to type cast / conversion input function
f_num = int(input("Enter first number : "))
s_num = int(input("Enter second number : "))

result = f_num + s_num
print("Sum is",result)
