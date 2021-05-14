try:
    file = open('file_1.txt','w')
    file.write("Hello")
    data = file.read()
    print(data)
    # file.close()
except BaseException as ex:
    print(ex)
finally:
    print("Finally will always execute")
    file.close()