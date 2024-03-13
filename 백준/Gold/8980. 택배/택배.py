n,t = map(int,input().split())
a = int(input())
arr = []
count = 0
for _ in range(a):
    b,c,d = map(int,input().split())
    arr.append([b,c,d])
size = [t for _ in range(n)]
arr.sort(key = lambda x : (x[1]))
for i in arr:
    #print(i,size)
    num = i[2]
    if min(size[(i[0]-1):i[1]-1]) < num:
        num = min(size[(i[0]-1):i[1]-1])
    for j in range(i[0]-1,i[1]-1):
        size[j] -= num
    count += num
print(count)