a,b = map(int,input().split())
g = 1
for i in range(1,b+1) :
    if i%a ==0 :
        g *= i
print(g)