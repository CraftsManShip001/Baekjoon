n = int(input())
arr = []
plus = []
minus = []
remover = 0
cnt = 0
for _ in range(n):
    a = int(input())
    if a < 0:
        minus.append(a*-1)
    elif a > 1:
        plus.append(a)
    elif a == 1:
        cnt += a
    else:
        remover += 1
minus.sort(reverse=True)
plus.sort(reverse=True)
if len(minus) % 2:
    if remover > 0:
        minus.pop(-1)
        remover -= 1
    else:
        cnt -= minus.pop(-1)
if len(plus) % 2:
    cnt += plus.pop(-1)
if len(minus) >= 2:
    for i in range(0,len(minus),2):
        cnt += (minus[i] * minus[i+1])
if len(plus) >= 2:
    for i in range(0,len(plus),2):
        cnt += (plus[i] * plus[i+1])
print(cnt)