def ispn(a):
    if a==2 or a==3:
        return True
    for i in range(2,a):
        if a%i==0 :
            return False
    return True

n = int(input())
if ispn(n) :
    print("P")
else :
    print("C")