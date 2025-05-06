n,x = map(int, input().split())
arr = list(map(int, input().split()))
res = []
for i in range(n-1):
    res.append((arr[i] + arr[i + 1]) * x)
print(min(res))