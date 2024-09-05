n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [-5001 for _ in range(m+1)]
for i in range(n-1, -1, -1):
    num = arr[i]
    for j in range(num, m+1):
        dp[j] = max(dp[j-num]*10+i, i, dp[j])
print(dp[m])