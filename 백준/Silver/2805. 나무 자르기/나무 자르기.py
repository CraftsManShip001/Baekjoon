n,h = map(int,input().split())
arr = list(map(int,input().split()))
low = 0
high = max(arr)
before = 0
while low <= high:
    mid = (low+high) // 2
    count  = 0
    for i in range(n):
        if arr[i] > mid:
            count += arr[i] - mid
    if   count >= h:
        if before < mid:
            before = mid
        low = mid + 1
    else:
        high = mid - 1
print(before)