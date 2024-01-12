cnt = 0
g = 1
n = int(input())
while True:
    if g==n :
        print(cnt)
        break
    else :
        g*=2
        cnt+=1