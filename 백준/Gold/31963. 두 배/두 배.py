import math
n = int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(n)]
cnt = 0
for i in range(1,n):
    num = math.ceil(math.log2(arr[i-1]/arr[i]))+dp[i-1]
    if num > 0:
        dp[i] = max(0, num)
        cnt += dp[i]
print(cnt)