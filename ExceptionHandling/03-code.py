def atm():
    total = 10000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success")
    else:
        # print("Login Failed")
        raise ValueError("Login Failed")

    amount = int(input("Enter the amount : "))
    if amount > total:
        raise ValueError("Insufficient balance")
    else:
        total -= amount
        print("Remaining balance is",total)

try:
    atm()
except ValueError as err:
    print(err)