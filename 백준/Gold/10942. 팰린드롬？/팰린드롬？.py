import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for x in range(n):
    for i in range(n-x):
        j = i + x
        if i == j:
            dp[i][j] = 1
        elif arr[i] == arr[j]:
            if i == (j-1):
                dp[i][j] = 1
            elif dp[i+1][j-1]:
                dp[i][j] = 1

for _ in range(m):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])
    