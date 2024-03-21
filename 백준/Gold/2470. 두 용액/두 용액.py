a = int(input())
arr = sorted(list(map(int,input().split())))
min = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999

left = 0
right = a-1
x = 0
y = 0

while left < right:
    if abs(arr[left] + arr[right]) < min:
        min = abs(arr[left] + arr[right])
        x = arr[left]
        y = arr[right]
    if arr[left] + arr[right] > 0:
        right -= 1
    elif arr[left] + arr[right] < 0:
        left += 1
    elif arr[left] + arr[right] == 0:
        x = arr[left]
        y = arr[right]
        break
print(x,y)