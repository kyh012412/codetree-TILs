n = int(input())
g = 1
i = 1
while True :
    g *= i
    if g>=n :
        print(i)
        break
    else :
        i += 1