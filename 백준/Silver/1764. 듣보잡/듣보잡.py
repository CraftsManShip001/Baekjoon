n,m = map(int,input().split())

cnt = 0
arr = {}
ans = []

for _ in range(n):
    a = input()
    arr[a] = 1
for _ in range(m):
    a = input()
    try:
        if arr[a]:
            cnt += 1
            ans.append(a)
    except:
        pass
print(cnt)

ans.sort()

for i in ans:
    print(i)