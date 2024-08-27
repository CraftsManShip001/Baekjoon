n,h = map(int,input().split())
arr = [0] * h
for i in range(n):
    num = int(input())
    if i % 2:
        arr[0] += 1
        arr[num] -= 1
    else:
        arr[h-num] += 1
for i in range(1, h):
    arr[i] += arr[i-1]
low = min(arr)
print(low,arr.count(low))