import sys, heapq
heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline()) * -1
	if num == 0:
		print(heapq.heappop(heap) * -1 if heap else 0)
	else:
		heapq.heappush(heap, num)