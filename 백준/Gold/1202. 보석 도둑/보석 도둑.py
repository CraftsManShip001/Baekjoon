import sys
import heapq
input=sys.stdin.readline
n,k = map(int,input().split())
arr = []
bag = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
for _ in range(k):
    bag.append(int(input()))
arr.sort()
bag.sort()
res = 0
tmp = []
 
for bag in bag:
    while arr and arr[0][0] <= bag:
        heapq.heappush(tmp, -arr[0][1])
        heapq.heappop(arr)
    if tmp:
        res -= heapq.heappop(tmp)
print(res)