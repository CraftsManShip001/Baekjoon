n,m,b = map(int,input().split())
arr = []
min_high = 1e9
min_time = 1e9
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
for i in range(257):
    cnt = 0
    count = b
    for l in range(n):
        for j in range(m):
            if arr[l][j] > i:
                cnt += (arr[l][j] - i) * 2
                count += arr[l][j] - i
            else:
                cnt += (i - arr[l][j])
                count -= (i - arr[l][j])
    if count < 0:
        break
    if min_time >= cnt:
        min_time = cnt
        min_high = i
print(min_time,min_high)