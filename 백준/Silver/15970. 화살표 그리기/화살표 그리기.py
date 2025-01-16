n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x : (x[0]))
cnt = 0
for i in range(n):
    m = 10**5 + 1
    for j in range(n):
        if i != j and arr[i][1] == arr[j][1] and abs(arr[i][0] - arr[j][0]) < m:
            m = abs(arr[i][0] - arr[j][0])
    cnt += m
print(cnt)