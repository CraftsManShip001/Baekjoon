n = int(input())
arr = {}
clubs = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
for i in range(9):
  m = list(map(int, input().split()))
  arr[clubs[i]] = max(m)
res = list(arr.values())
m = res.index(max(res))
print(clubs[m])