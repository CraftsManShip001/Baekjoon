import sys
input = lambda: sys.stdin.readline().rstrip()
MA = 1000000007
def sege_make(start,end,index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    else:
        mid = (start + end) // 2
        tree[index] = sege_make(start,mid,index * 2) * sege_make(mid+1,end,index * 2 + 1) % MA
        return tree[index]

def sege_mul(start,end,index,left,right):
    if left > end or right < start:
        return 1
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return sege_mul(start,mid,index * 2,left,right) * sege_mul(mid + 1,end,index * 2 + 1,left,right) % MA

def sege_update(start,end,index,what,value):
    if what < start or what > end:
        return tree[index]
    if start == end:
        tree[index] = value
        return value
        
    mid = (start + end) // 2
    
    l = sege_update(start,mid,index*2,what,value)
    r = sege_update(mid + 1,end,index * 2 + 1,what,value)
    tree[index] = (l * r) % MA
    return tree[index]

n,m,k = map(int,input().split())
arr = []
tree = [0] * (n * 4)
for _ in range(n):
    arr.append(int(input()))
sege_make(0,n-1,1)
for _ in range(m + k):
    a,b,c = map(int,input().split())
    if a == 1:
        sege_update(0,n-1,1,b-1,c)
        arr[b-1] = c
    else:
        print(sege_mul(0,n-1,1,b-1,c-1) % MA)