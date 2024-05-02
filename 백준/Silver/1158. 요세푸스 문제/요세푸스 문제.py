a,b = map(int,input().split())
arr = [i for i in range(1,a+1)]
print('<',end = '')
i = b -1
res = []
while arr:
    i = i % len(arr)
    c = str(arr.pop(i))
    res.append(c)
    i = i + (b - 1)
print(', '.join(res),end = '')
print('>')