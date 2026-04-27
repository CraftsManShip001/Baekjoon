import sys
input = sys.stdin.readline
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return x
def union(a, b):
    x, y = find(a), find(b)
    if x<y: parent[x] = y
    else: parent[y] = x
def upper_bound(num):
    start, end = 0, M-1
    while start <= end:
        mid = (start + end) // 2
        if minsu[mid] <= num:
            start = mid+1
        else:
            end = mid-1
    return start

N, M, K = map(int,input().split())
parent = [i for i in range(N)]

minsu = list(map(int,input().split()))
cheolsu = list(map(int,input().split()))

minsu.sort()

for c in cheolsu:
    idx = upper_bound(c)
    idx = find(idx)
    print(minsu[idx])
    union(idx, idx+1)