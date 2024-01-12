n = int(input())
for i in range(0,n):
    for j in range(0,n-i):
        for k in range(0,n-i):
            print("*",end="")
        print(" ",end="")
    print()