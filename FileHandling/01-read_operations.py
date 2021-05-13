file = open('file_handling_notes.txt')

# data = file.read()

# file.seek(20)
# data = file.read(20)

# data = file.readline()

data = file.readlines()
print(data)

file.close()
