n, k = map(int,input().split())
dp = [[0] * 201 for _ in range(201)]
for x in range(201):
    dp[1][x] = 1
    dp[2][x] = x+1
for i in range(3, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000
print(dp[k][n])