n,h = map(int, input().split())
d = [0] + list(map(int, input().split()))
s = [0] * (n + 1)
for k in range(1, n + 1):
    s[k] = s[k - 1] + d[k]
if h > s[-1]:
    print(-1)
else:
    for i in range(1, n + 1):
        if h <= s[i]:
            print(i)
            break