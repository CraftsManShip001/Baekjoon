from collections import deque
 
T = int(input())
results = []
 
for _ in range(T):
    h, w = map(int, input().split())
    graph = []
    graph.append(["." for _ in range(w+2)])
    for _ in range(h):
        graph.append(list("."+input()+"."))
    graph.append(["." for _ in range(w+2)])
 
    keys = [0 for _ in range(26)]
    for k in list(input()):
        if k != "0":
            keys[ord(k) - 97] = 1
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    deq = deque([(0,0)])
    papers = 0
    tempDoors = [[] for _ in range(26)]
 
    while deq:
        r, c = deq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < h+2 and 0 <= nc < w+2 and graph[nr][nc] != "*":
                num = ord(graph[nr][nc])
                if 65 <= num <= 90:
                    if keys[num - 65] == 0:
                        tempDoors[num - 65].append((nr, nc))
                        continue
                elif 97 <= num <= 122:
                    if keys[num - 97] == 0:
                        for door in tempDoors[num - 97]:
                            deq.appendleft(door)
                    keys[num - 97] = 1
                elif graph[nr][nc] == "$":
                    papers += 1
                
                graph[nr][nc] = "*"
                deq.append((nr, nc))
    results.append(papers)
    
for r in results:
    print(r)