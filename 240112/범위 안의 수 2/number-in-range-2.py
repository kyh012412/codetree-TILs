s =0
c = 0
for _ in range(10):
    a = int(input())
    if a>=0 and a<=200 :
        s+=a
        c+=1
print(f"{s} {s/c:.1f}")