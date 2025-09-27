with open("archivo.txt", "w") as file:
    for i in range(1,100):
        file.write(f"Line: {i}\n")
    

with open("archivo.txt","r") as file:
    lines = file.readlines()
    for line in lines: 
        print(line)