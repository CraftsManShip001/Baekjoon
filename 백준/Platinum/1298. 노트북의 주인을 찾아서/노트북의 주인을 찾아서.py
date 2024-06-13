import sys
input = sys.stdin.readline
def dfs(num):
    if visited[num] or num == -1:
        return False
    visited[num] = True
    for main in arr[num]:
        if select[main] == -1 or dfs(select[main]):
            select[main] = num
            return True
    return False
n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
select = [-1 for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)
cnt = 0
for l in range(1,n+1):
    if select[l] != -1:
        cnt += 1
print(cnt)