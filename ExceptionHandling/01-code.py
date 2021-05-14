try:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    a = x + y
    b = x - y
    c = x / y
    d = x * y
except ZeroDivisionError as err:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input...")
except BaseException as ex:
    print("Error :",ex)

else:
    print("Sum is", a)
    print("Sub is", b)
    print("Div is", c)
    print("Mul is", d)