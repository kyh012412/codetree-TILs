def isf(a):
    if a%2==0 or a%3==0 or a%5==0:
        return True
    return False

n = int(input())
cnt = 0
for i in range(1,n+1):
    if isf(i) == False :
        cnt +=1
print(cnt)