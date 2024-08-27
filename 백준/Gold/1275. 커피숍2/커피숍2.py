def sege_make(start,end,index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    else:
        mid = (start + end) // 2
        tree[index] = sege_make(start,mid,index * 2) + sege_make(mid+1,end,index * 2 + 1)
        return tree[index]

def sege_sum(start,end,index,left,right):
    if left > end or right < start:
        return 0
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return sege_sum(start,mid,index * 2,left,right) + sege_sum(mid + 1,end,index * 2 + 1,left,right)

def sege_update(start,end,index,what,value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    
    sege_update(start,mid,index*2,what,value)
    sege_update(mid + 1,end,index * 2 + 1,what,value)
    
n,q = map(int,input().split())
arr = list(map(int,input().split()))
tree = [0] * (n * 4)
sege_make(0,n-1,1)
for _ in range(q):
    x,y,a,b = map(int,input().split())
    if x < y:
        print(sege_sum(0,n-1,1,x-1,y-1))
    else:
        print(sege_sum(0,n-1,1,y-1,x-1))
    sege_update(0,n-1,1,a-1,b-arr[a-1])
    arr[a-1] = b