n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in range((n-k)+1):
    ans.append(sum(arr[i:i+k]))
print(max(ans))