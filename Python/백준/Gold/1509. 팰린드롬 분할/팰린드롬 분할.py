import sys

sys.setrecursionlimit(10 ** 8)


string = sys.stdin.readline().rstrip()
n = len(string)
palindrome = [[0 for _ in range(n)] for _ in range(n)]
dp = [2500] * (n+1)
dp[-1] = 0
for i in range(n):
    palindrome[i][i] = 1

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if string[i] == string[j]:
            if j - i == 1:
                palindrome[i][j] = 1
            else:
                palindrome[i][j] = palindrome[i + 1][j - 1]

for end in range(n):
    for start in range(end + 1):
        if palindrome[start][end]:
            dp[end] = min(dp[end], dp[start-1]+1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)
print(dp[n-1])