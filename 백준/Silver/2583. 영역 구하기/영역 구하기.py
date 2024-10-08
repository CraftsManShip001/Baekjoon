from collections import deque
m,n,k = map(int,input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    a,b,c,d = map(int,input().split())
    for i in range(b,d):
        for j in range(a,c):
            arr[i][j] = 1
d = [[0,1],[1,0],[0,-1],[-1,0]]
count = 0
an = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            q = deque()
            q.append((i,j))
            arr[i][j]=2
            cnt = 1
            while q:
                x,y = q.popleft()
                for dx,dy in d:
                    nx=x + dx
                    ny = y + dy
                    if nx >= m or ny >= n or nx < 0 or ny < 0:
                        continue
                    if arr[nx][ny] == 0:
                        cnt += 1
                        arr[nx][ny] = 2
                        q.append((nx,ny))
            an.append(cnt)
print(len(an))
an.sort()
for l in an:
    print(l,end = ' ')