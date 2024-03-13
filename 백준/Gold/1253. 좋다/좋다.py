n = int(input())
count = 0
arr = list(map(int,input().split()))
arr.sort()

for i in range(len(arr)):
    temp = arr[:i] + arr[i + 1:]
    left = 0
    right = len(temp)-1
    while left != right:
        if temp[left] + temp[right] == arr[i]:
            count += 1
            break
        elif temp[left] + temp[right] > arr[i]:
            right -= 1
        else:
            left += 1
        
print(count)