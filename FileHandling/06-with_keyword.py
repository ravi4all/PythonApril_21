# file = open('file_1.txt')
# data = file.read()
# print(data)
# file.close()

with open('file_1.txt') as file:
    data = file.read()
    print(data)
