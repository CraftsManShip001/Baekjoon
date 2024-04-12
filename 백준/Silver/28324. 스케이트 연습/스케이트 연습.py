a=int(input())
b=list(map(int,input().split()))
b[-1]=1
for i in range(a-1,0,-1):
    if b[i-1]-b[i]>1:
        b[i-1]=b[i]+1
print(sum(b))