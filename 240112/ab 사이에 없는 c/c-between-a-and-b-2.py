a,b,c = map(int,input().split())
bv = False
for i in range(a,b+1):
    if i%c==0 :
        bv = True
        break
if bv :
    print("NO")
else :
    print("YES")