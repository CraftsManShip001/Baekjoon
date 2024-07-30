import sys
sys.setrecursionlimit(10000)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y,c):
    for l in range(4):
        px = dx[l] + x
        py = dy[l] + y
        if 0 <= px < n and 0 <= py < n:
            if arr[px][py] == c and visit[px][py] == 0:
                visit[px][py] = 1
                dfs(px,py,c)
def dfs_D(x,y,c):
    for l in range(4):
        px = dx[l] + x
        py = dy[l] + y
        if 0 <= px < n and 0 <= py < n:
            if arr2[px][py] == c and visit[px][py] == 0:
                visit[px][py] = 1
                dfs_D(px,py,c)
n = int(input())
arr = []
arr2 = []
for _ in range(n):
    a = list(input())
    b = []
    for i in a:
        if i == 'G':
            b.append('R')
        else:
            b.append(i)
    arr.append(a)
    arr2.append(b)
visit = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            dfs(i,j,arr[i][j])
            cnt += 1
print(cnt,end = ' ')
visit = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            dfs_D(i,j,arr2[i][j])
            cnt += 1
print(cnt)