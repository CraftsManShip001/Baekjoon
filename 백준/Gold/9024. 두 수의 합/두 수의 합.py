t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    left = 0
    right = n-1
    an = []
    while left < right:
        mid = arr[left] + arr[right]
        if mid < k:
            left += 1
            an.append(abs(mid-k))
        elif mid > k:
            right -= 1
            an.append(abs(mid-k))
        else:
            left += 1
            an.append(0)
    print(an.count(min(an)))