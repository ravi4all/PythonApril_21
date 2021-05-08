# def emp(id, name, age, sal, *address):
#     print(f"Id is {id}")
#     print(f"Name is {name}")
#     print(f"Age is {age}")
#     print(f"Salary is {sal}")
#     print(f"Address is {address}")
#
# emp(101,'John',45,56000,'US')
# emp(101,'John',45,56000,'US','UK')
# emp(101,'John',45,56000,'US','IN','FR')

def emp(**details):
    print(details)

emp(name = 'John')
emp(id = 101, name = 'Sam', age = 44)
emp(id = 102, name = 'Mac', sal = 45000, address = 'Delhi')
