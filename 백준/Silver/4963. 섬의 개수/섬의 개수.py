import sys
sys.setrecursionlimit(10000)
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
def dfs(x,y):
    for l in range(8):
        px = x + dx[l]
        py = y + dy[l]
        if 0 <= px < h and 0 <= py < w:
            if arr[px][py] == 1 and visit[px][py] == 0:
                visit[px][py] = 1
                dfs(px,py)
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        quit()
    arr = []
    for i in range(h):
        arr.append(list(map(int,input().split())))
    visit = [[0] * w for i in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and arr[i][j] == 1:
                visit[i][j] = 1
                dfs(i,j)
                cnt += 1
    print(cnt)