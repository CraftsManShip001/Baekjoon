from collections import deque
n, k = map(int, input().split())
visited = [0 for _ in range((10 ** 5)+1)]
visit = {}
an = deque()
an.append(n)
while an:
    now = an.popleft()
    if now == k:
        print(visited[k])
        ans = [k]
        while True:
            if not k in visit or k == n:
                break
            else:
                ans.append(visit[k])
                k = visit[k]
        ans.reverse()
        print(*ans)
        break
    arr = [now+1,now-1,now*2]
    for i in arr:
        if 0 <= i <= (10 ** 5) and visited[i] == 0: 
            visited[i] = visited[now] + 1
            visit[i] = now
            an.append(i)