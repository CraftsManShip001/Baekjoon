x,y = map(int, input().split())
n = int(input())
arr = [x/y]
for _ in range(n):
    x,y = map(int, input().split())
    arr.append(x/y)
print("%.2f" % (min(arr) * 1000))