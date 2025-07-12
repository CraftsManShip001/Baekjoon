a = list(input())
b = list(input())

lena = len(a) + 1
lenb = len(b) + 1

dp = [[""] * lenb for _ in range(lena)]
for i in range(1,lena):
    for j in range(1, lenb):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else:
            if len(dp[i][j-1]) <= len(dp[i-1][j]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[-1][-1]) != 0:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
else:
    print(0)