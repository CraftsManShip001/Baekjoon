import sys
sys.setrecursionlimit(10000)
def dfs(idx):
    global visit
    for j in graph[idx]:
        if visit[j] != 1:
            visit[j] = 1
            dfs(j)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visit = [0 for _ in range(n+1)]
for i in range(1,n+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)