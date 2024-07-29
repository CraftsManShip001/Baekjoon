from collections import deque
n, k = map(int, input().split())
visited = [0 for _ in range((10 ** 5)+1)]
ans = [0 for _ in range((10 ** 5) + 1)]
an = deque()
an.append(n)
ans[n] = 1
while an:
    now = an.popleft()
    if now == k:
        print(visited[k])
        print(ans[k])
        break
    arr = [now+1,now-1,now*2]
    for i in arr:
        if 0 <= i <= (10 ** 5):
            if visited[i] == 0: 
                visited[i] = visited[now] + 1
                ans[i] = ans[now]
                an.append(i)
            elif visited[i] == visited[now] + 1:
                ans[i] += ans[now]
        