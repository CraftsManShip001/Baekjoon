n = int(input())
m = int(input())
arr = []
cnt = 0
for _ in range(n-1):
    arr.append(int(input()))

while True:
    x = -1
    idx = -1
    for i in range(n-1):
        if arr[i] >= x:
            idx = i
            x = arr[i]
    if idx == -1:
        break
    if x < m:
        break
    else:
        arr[idx] -= 1
        m += 1
        cnt += 1

print(cnt)