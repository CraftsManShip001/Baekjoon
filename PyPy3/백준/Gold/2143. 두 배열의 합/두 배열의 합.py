from collections import Counter
t = int(input())
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
ans = 0
cnt = Counter()
for x in range(n):
    for y in range(x,n):
        cnt[sum(arr1[x:y+1])] += 1
for x in range(m):
    for y in range(x,m):
        res = t - sum(arr2[x:y+1]) 
        ans += cnt[res] 
print(ans)