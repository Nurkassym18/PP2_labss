file = open("111.txt","r")
print(file.read())
file.seek(0)

print(file.readline())
file.seek(0)


for row in file :
    print(row)
file.seek(0)


for row in file:
    for letter in row:
        print(letter)
file.seek(0)


file_readlines=file.readlines()
print(file_readlines)
file.seek(0)
