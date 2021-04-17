#If-Else Expression
x,y = 10,20

condition = "X is greater" if x > y else "Y is greater"
print(condition)


x,y,z = 10,20,30
condition = "X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(condition,"is greater")
