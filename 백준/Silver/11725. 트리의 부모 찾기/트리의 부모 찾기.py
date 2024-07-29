n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n + 1)]
arr = [1]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
while len(arr):
    now = arr.pop(-1)
    for v in graph[now]:
        if parent[v] == 0:
            parent[v] = now
            arr.append(v)
for i in range(2,n+1):
    print(parent[i])