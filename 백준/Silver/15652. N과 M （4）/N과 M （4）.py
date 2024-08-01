def back(arr,idx):
    global res
    if idx > m:
        res.append(arr)
        return 0
    else:
        if idx == 1:
            num = 1
        else:
            num = arr[-1]
        for i in range(num,n+1):
            back(arr + [i], idx + 1)
n,m = map(int,input().split())
res = []
back([],1)
for i in res:
    print(*i)