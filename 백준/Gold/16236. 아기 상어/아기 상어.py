import sys
sys.setrecursionlimit(10**9)
from collections import deque
input=sys.stdin.readline
def bfs(now_x,now_y):
    global visit
    array = deque()
    array.append([now_x,now_y])
    temp = []
    idx = 0
    while array:
        idx += 1
        x,y = array.popleft()
        for i in range(4):
            px = dx[i] + x
            py = dy[i] + y
            if 0 <= px < n and 0 <= py < n:
                if arr[px][py] <= size:
                    if visit[px][py] == -1:
                        visit[px][py] = visit[x][y] + 1
                        array.append([px,py])
                        if arr[px][py] < size and arr[px][py] != 0:
                            temp.append([visit[px][py],px,py])
    return temp
n = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
size = 2
fish = 0
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    if a.count(9):
        shark_x = i
        shark_y = a.index(9)
        a[shark_y] = 0
    arr.append(a)
#print()
while True:
    visit = [[-1] * n for _ in range(n)]
    visit[shark_x][shark_y] = 0
    result = bfs(shark_x,shark_y)
    if len(result):
        result.sort()
        #print(result)
        cnt += result[0][0]
        shark_x = result[0][1]
        shark_y = result[0][2]
        arr[shark_x][shark_y] = 0
        fish += 1
    else:
        break
    if fish == size:
        size += 1
        fish = 0
print(cnt)