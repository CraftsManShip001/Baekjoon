n = int(input())
arr = [0 for _ in range(n*2)]
m = 0
cnt = 0
for i in list(map(int,input().split())):
    if not arr[i]:
        cnt+=1
        m = max(cnt,m)
        arr[i] = 1
    else:
        cnt-=1
print(m)