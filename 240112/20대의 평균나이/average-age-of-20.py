s =0
c =0
while True:
    n = int(input())
    if n>=30 or n<20:
        break
    s += n
    c += 1
print(f"{s/c:.2f}")