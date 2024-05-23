n = int(input())
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
arr.sort(key = lambda x : (x[0],x[1]))
for i in arr:
    print(i[0],i[1])