ass,ae = map(int,input().split())
bs,be = map(int,input().split())
if ass>bs :
    print("A")
elif bs>ass :
    print("B")
else :
    if ae>be :
        print("A")
    elif be>ae :
        print("B")