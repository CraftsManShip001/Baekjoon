n = int(input())
arr = []
res = 0
for i in range(n):
    a = list(map(int,input().split(' ')))
    arr.append(a)
arr.append(arr[0])
for i in range(n):
    res += arr[i][0] * arr[i+1][1] - (arr[i+1][0] * arr[i][1])
print(abs(res)/2)