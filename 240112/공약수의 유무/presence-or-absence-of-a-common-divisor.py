a,b = map(int,input().split())
bv = False
for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0 :
        bv=True
        break
print(int(bv))