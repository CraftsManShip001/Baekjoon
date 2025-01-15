n = int(input())
dic = {136:1000,142:5000,148:10000,154:50000}
cnt = 0
for _ in range(n):
    a,b = map(int,input().split())
    cnt += dic[a]
print(cnt)