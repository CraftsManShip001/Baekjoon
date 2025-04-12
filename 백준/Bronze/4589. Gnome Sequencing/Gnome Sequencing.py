n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
print("Gnomes:")
for i in arr:
    if i == sorted(i) or i == sorted(i, reverse=True):
        print("Ordered")
    else:
        print("Unordered")