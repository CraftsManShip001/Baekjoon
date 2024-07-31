n,m = map(int,input().split())
tlist = set(input().split()[1:])
arr = []
cnt = 0
for _ in range(m):
    a = set(input().split()[1:])
    arr.append(a)
for i in range(m):
    for j in arr:
        if j.intersection(tlist):
            tlist = j.union(tlist)
for i in arr:
    if i.intersection(tlist):
        pass
    else:
        cnt += 1
print(cnt)