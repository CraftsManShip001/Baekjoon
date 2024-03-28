n = 5
arr = []
cnt = 0
for i in range(n):
    a = int(input())
    arr.append(a)
    cnt += a
arr.sort()
print(cnt // n)
print(arr[n//2])