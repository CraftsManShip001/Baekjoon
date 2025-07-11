c, n = map(int, input().split())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort()
dp = [0] + [1000000] * (c + 101)
cnt = 999999

for x,y in arr:
    for i in range(y, len(dp)):
        dp[i] = min(dp[i - y] + x, dp[i])
        if i >= c:
            cnt = min(dp[i], cnt)

print(cnt)