n = int(input())
s = 0
i = 1
while True :
    s += i
    if s>=n :
        print(i)
        break
    else :
        i+=1