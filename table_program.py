n = int(input("Enter the number : "))

for i in range(1,11):
    print('{} x {} = {}'.format(n, i, n * i))

x = 0
for i in range(n):
    #x += 1
    x = x + 1
print("Sum is",x)
