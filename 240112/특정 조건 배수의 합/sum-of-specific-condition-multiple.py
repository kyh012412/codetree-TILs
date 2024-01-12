a,b = map(int,input().split())
s = 0
arr = [a,b]
a = arr[0]
b = arr[1]
for i in range(a,b+1):
    if i%5==0:
        s += i
print(s)