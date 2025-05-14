arr = ['G...', '.I.T', '..S.']
k = int(input())
for x in arr: 
    res = ''
    for j in range(len(x)) : 
        res += (x[j] * k)
    for _ in range(k) : 
        print(res)