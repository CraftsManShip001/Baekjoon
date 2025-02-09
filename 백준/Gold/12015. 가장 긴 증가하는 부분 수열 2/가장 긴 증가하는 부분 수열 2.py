def 이분탐색(arr, x):
    left,right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

n = int(input())
arr = list(map(int, input().split()))

res = [0]
for i in range(n):
    if res[-1] < arr[i]:
        res.append(arr[i])
    elif res[-1] > arr[i]:
        idx = 이분탐색(res, arr[i])
        res[idx] = arr[i]

print(len(res)-1)