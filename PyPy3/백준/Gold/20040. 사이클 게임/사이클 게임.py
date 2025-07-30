import sys
input = sys.stdin.readline
def find(num):
    while num!= arr[num]:
        num = arr[num]
    return num
n, m = map(int, input().split())
arr = [x for x in range(n)]
ans = 0
for i in range(1, m+1):
    a,b = map(int, input().split())
    x = find(a)
    y = find(b)
    if x == y:
        ans = i
        break
    if x < y:
        arr[y] = x
    else:
        arr[x] = y
print(ans)