cnt=0
n = int(input())
i=1
while i<=n:
    if i%4==0 :
        if i%100!=0 :
            cnt+=1
        else :
            if i%400==0 :
                cnt+=1
    i+=1
print(cnt)