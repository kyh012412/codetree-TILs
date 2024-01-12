def iso(a):
    if a%2==0 :
        return False
    if a%10==5 :
        return False
    if a%3==0 and a%9 !=0 :
        return False
    return True

n = int(input())
for i in range(1,n+1) :
    if iso(i) :
        print(i,end=" ")