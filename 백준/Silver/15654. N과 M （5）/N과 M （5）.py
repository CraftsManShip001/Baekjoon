def back(arr,idx):
    global res
    if idx > m:
        res.append(arr)
        return 0
    else:
        for i in range(n):
            if not main[i] in arr:
                back(arr + [main[i]], idx + 1)
n,m = map(int,input().split())
main = list(map(int,input().split()))
main.sort()
res = []
back([],1)
for i in res:
    print(*i)