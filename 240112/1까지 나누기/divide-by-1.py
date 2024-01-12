n = int(input())
cnt = 1
while True :
    n = n//cnt
    if n<=1 :
        print(cnt)
        break
    else :
        cnt += 1