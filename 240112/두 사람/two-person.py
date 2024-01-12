f = input().split()
s = input().split()

fa = int(f[0])
sa = int(s[0])

if (fa>=19 and f[1] == 'M') or (sa>=19 and s[1]=='M'):
    print(1)
else :
    print(0)