n, m = map(int, input().split())
arr = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1
for i in range(1, n+1):
    print(arr[i])