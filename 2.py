#4
file = open("112.txt","r")
count_row = 0
for row in file:
    count_row = count_row + 1
print(count_row)
file.seek(0)
count_row2=sum(1 for row in file  )
print(count_row2)
#5
Mylist = ["Hello","Hi"]
with open("list.txt","w") as file:
    for i in Mylist:
        file.write(i + "\n")
#6 
for i in range(1,27):
    with open(f"{chr(64+i)}.txt", "w") as file:
        file.write("hello ")