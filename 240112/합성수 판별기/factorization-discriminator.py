def ish(a):
    if a==2 or a==3 :
        return False
    if a>=4 :
        for i in range(2,a) :
            if a%i==0 :
                return True
    return False

n = int(input())
if ish(n) :
    print('C')
else :
    print('N')