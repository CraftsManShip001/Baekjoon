'''
def sege_make_max(start,end,index):
    if start == end:
        tree_max[index] = arr[start]
        return tree_max[index]
    else:
        mid = (start + end) // 2
        tree_max[index] = max(sege_make_max(start,mid,index * 2), sege_make_max(mid+1,end,index * 2 + 1))
        return tree_max[index]'''
    
def sege_make_min(start,end,index):
    if start == end:
        tree_min[index] = arr[start]
        return tree_min[index]
    else:
        mid = (start + end) // 2
        tree_min[index] = min(sege_make_min(start,mid,index * 2), sege_make_min(mid+1,end,index * 2 + 1))
        return tree_min[index]
'''
def sege_max(start,end,index,left,right):
    if left > end or right < start:
        return 0
    if start >= left and end <= right:
        return tree_max[index]
    mid = (start + end) // 2
    return max(sege_max(start,mid,index * 2,left,right), sege_max(mid + 1,end,index * 2 + 1,left,right))'''

def sege_min(start,end,index,left,right):
    if left > end or right < start:
        return 1000000000
    if start >= left and end <= right:
        return tree_min[index]
    mid = (start + end) // 2
    return min(sege_min(start,mid,index * 2,left,right), sege_min(mid + 1,end,index * 2 + 1,left,right))
    
n,m = map(int,input().split())
arr = []
tree_min = [1000000000] * (n * 4)
#tree_max = [0] * (n * 4)
for _ in range(n):
    arr.append(int(input()))
sege_make_min(0,n-1,1)
#sege_make_max(0,n-1,1)
for _ in range(m):
    a,b = map(int,input().split())
    print(sege_min(0,n-1,1,a-1,b-1))