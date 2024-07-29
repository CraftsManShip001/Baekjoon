from collections import deque
n, k = map(int, input().split())
visited = [0 for _ in range((10 ** 5)+1)]
an = deque()
an.append(n)
if (n * 2) == k:
    print(0)
    quit()
while an:
    now = an.popleft()
    if now == k:
        print(visited[k])
        break
    arr = [now * 2]
    for i in arr:
        if 0 <= i <= (10 ** 5):
            if visited[i] > visited[now] or visited[i] == 0: 
                visited[i] = visited[now]
                an.append(i)
    arr = [now+1,now-1]
    for i in arr:
        if 0 <= i <= (10 ** 5):
            if visited[i] > (visited[now] + 1) or visited[i] == 0: 
                visited[i] = visited[now] + 1
                an.append(i)