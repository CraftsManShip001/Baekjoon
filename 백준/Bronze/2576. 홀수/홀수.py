arr = []
for i in range(7):
    a = int(input())
    if 1&a:
        arr.append(a)
if len(arr):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)