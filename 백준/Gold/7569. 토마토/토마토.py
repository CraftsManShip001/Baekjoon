import copy
import sys
from collections import deque
input = sys.stdin.readline
def bfs(z,x,y):
    global arr,back
    for i in range(6):
        if dx[i] + x < m and dy[i] + y < n and dx[i] + x >= 0 and dy[i] + y >= 0 and dh[i] + z < h and dh[i] + z >= 0:
            if arr[dh[i] + z][dx[i] + x][dy[i] + y] == 0:
                arr[dh[i] + z][dx[i] + x][dy[i] + y] = arr[z][x][y] + 1
                back.append([dh[i] + z,dx[i] + x, dy[i] + y])
    return 0
n,m,h = map(int,input().split())
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]
back = deque()
arr = [[] for _ in range(h)]
for i in range(m * h):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        if a[j] == 1:
            back.append([i//m,i - ((i//m) * m),j])
    arr[i//m].append(a)
while back:
    z,x,y = back.popleft()
    bfs(z,x,y)
result = 0
for i in arr:
    for j in i:
        for l in j:
            if l == 0:
                print(-1)
                quit()
        result = max(result,max(j))
print(result-1)