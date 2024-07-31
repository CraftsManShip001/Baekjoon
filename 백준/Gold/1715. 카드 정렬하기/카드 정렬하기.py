import heapq
n = int(input())
arr = []
cnt = 0
for _ in range(n):
    num = int(input())
    arr.append(num)
arr.sort()
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    cnt += (a + b)
    heapq.heappush(arr,a+b)
print(cnt)