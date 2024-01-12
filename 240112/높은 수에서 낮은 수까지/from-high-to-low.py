a,b = map(int,input().split())
mx = a if a>b else b
mn = a if a<b else a
for i in range(b,a-1,-1):
    print(i,end=" ")