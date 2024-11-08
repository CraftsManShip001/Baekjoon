n = int(input())
cnt = 0
for _ in range(n):
    a = list(map(int,input().split()))
    cnt += sum(a)
print(cnt)