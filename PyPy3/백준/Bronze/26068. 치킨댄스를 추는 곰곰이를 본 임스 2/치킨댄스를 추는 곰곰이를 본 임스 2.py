import sys; input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    n = int(input()[2:])
    if n <= 90:
        ans += 1
print(ans)