n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
for _ in range(m):
  i,j,k = map(int, input().split())
  arr = arr[:i-1] + arr[k-1:j] + arr[i-1:k-1] + arr[j:]
for ans in arr:
  print(ans, end=' ')