n = int(input())
arr = list(map(int,input().split()))
cnt = sorted(list(set(arr)))

find = {}

for x in range(len(cnt)):
    find[cnt[x]] = x

for x in arr:
    print(find[x],end = ' ')