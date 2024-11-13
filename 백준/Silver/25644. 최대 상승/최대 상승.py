n = int(input())
arr = list(map(int,input().split()))
m = arr[0]
res = 0
for i in arr:
    if m > i:
        m = i
    if res < (i - m):
        res = i - m
print(res)