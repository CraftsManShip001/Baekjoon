n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

arr = {}
cnt = 0

for x in A:
    for y in B:
        num = x + y
        if num in arr:
            arr[num] += 1
        else:
            arr[num] = 1

for x in C:
    for y in D:
        num = (x + y) * -1
        if num in arr:
            cnt += arr[num]

print(cnt)