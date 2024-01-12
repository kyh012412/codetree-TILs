arr = [0,0,0]
i=1
n = int(input())
while i<=n :
    if i%12==0 :
        arr[2]+=1
    elif i%3==0 :
        arr[1]+=1
    elif i%2==0 :
        arr[0] +=1
    i+=1
print(arr[0],arr[1],arr[2])