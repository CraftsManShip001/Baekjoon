n,p = map(int,input().split())
arr = list(map(int,input().split()))
al = n * p
for i in arr:
    print(i - al,end = ' ')