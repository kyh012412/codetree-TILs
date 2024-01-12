a,b,c = map(int,input().split())
arr = [a,b,c]
bv = False
for i in range(a,b+1):
    if i%c==0 :
        bv=True
        break
if bv :
    print("YES")
else :
    print("NO")