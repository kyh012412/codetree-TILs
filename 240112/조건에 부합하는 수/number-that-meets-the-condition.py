def isc(a):
    if a%2==0 and a%4!=0 :
        return True
    if (a//8)%2==0 :
        return True
    if a%7<4 :
        return True
    return False

a = int(input())
for i in range(1,a+1):
    if isc(i) == False :
        print(i,end=" ")