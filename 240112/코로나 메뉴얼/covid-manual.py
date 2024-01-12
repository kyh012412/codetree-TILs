a = input().split()
b = input().split()
c = input().split()
count = 0
temp = a
if int(temp[1])>=37 and temp[0]=='Y' :
    count = count+1

temp = b
if int(temp[1])>=37 and temp[0]=='Y' :
    count = count+1

temp = c
if int(temp[1])>=37 and temp[0]=='Y' :
    count = count+1

if count>=2 :
    print("E")
else :
    print("N")