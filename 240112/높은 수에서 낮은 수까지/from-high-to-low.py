a,b = map(int,input().split())
mx = a if a>b else b
mn = a if a<b else b
for i in range(mx,mn-1,-1):
    print(i,end=" ")