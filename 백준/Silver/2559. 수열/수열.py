n,k = map(int,input().split())
arr = list(map(int,input().split()))
s = 0
for i in range(k):
    s += arr[i]
m = s
idx = 0
for x in range(k,n):
    s -= arr[idx]
    s += arr[x]
    idx += 1
    if m < s:
        m = s
print(m)