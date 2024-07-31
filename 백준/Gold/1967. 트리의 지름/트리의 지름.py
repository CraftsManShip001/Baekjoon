import sys
sys.setrecursionlimit(10**9)

def dfs(x, cnt):
    for i in graph[x]:
        node = i[0]
        v = i[1]
        if visit[node] == -1:
            visit[node] = cnt + v
            dfs(node, cnt + v)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [-1 for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
visit[1] = 0
dfs(1,0)

idx = visit.index(max(visit))
visit = [-1 for _ in range(n+1)]
visit[idx] = 0
dfs(idx,0)

print(max(visit))