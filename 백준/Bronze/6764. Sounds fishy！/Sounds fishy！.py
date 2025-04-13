arr = [int(input()) for _ in range(4)]
n = 0
for i in range(3):
    if arr[i+1] > arr[i]:
        n += 1
    elif arr[i+1] < arr[i]:
        n -= 1

if len(set(arr)) == 1: 
    print("Fish At Constant Depth")
elif n == -3:    
    print("Fish Diving")
elif n == 3:
    print("Fish Rising")
else:
    print("No Fish")