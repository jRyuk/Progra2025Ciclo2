with open("archivo.txt","r") as file:
    file.seek(10)
    print(file.readline())
    print(file.tell())


