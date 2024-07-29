import copy
import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y):
    global arr,back
    for i in range(4):
        if dx[i] + x < m and dy[i] + y < n and dx[i] + x >= 0 and dy[i] + y >= 0:
            if arr[dx[i] + x][dy[i] + y] == 0:
                arr[dx[i] + x][dy[i] + y] = arr[x][y] + 1
                back.append([dx[i] + x, dy[i] + y])
    return 0
n,m = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
back = deque()
arr = []
c = 0
for i in range(m):
    a = list(map(int,input().split()))
    for q in range(n):
        if a[q] == 1:
            back.append([i,q])
    c += a.count(0)
    arr.append(a)
if c == 0:
    print(0)
    quit()
while back:
    x,y = back.popleft()
    bfs(x,y)
result = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            quit()
    result = max(result,max(i))
print(result-1)