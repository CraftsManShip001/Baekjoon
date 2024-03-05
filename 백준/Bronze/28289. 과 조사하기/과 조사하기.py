p = int(input())
arr = [0,0,0,0]
for _ in range(p):
    a,b,c = map(int,input().split())
    if a == 1:
        arr[3] += 1
    elif b == 1 or b == 2:
        arr[0] += 1
    elif b == 3:
        arr[1] += 1
    else:
        arr[2] += 1    
for i in arr:
    print(i)