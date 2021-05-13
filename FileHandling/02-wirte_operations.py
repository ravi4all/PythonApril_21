file = open('file_1.txt', 'w')

# data = "Hello world"

data = ["Hello\n", "Hi\n", "Hey\n"]
# file.write(data)
file.writelines(data)

file.close()
