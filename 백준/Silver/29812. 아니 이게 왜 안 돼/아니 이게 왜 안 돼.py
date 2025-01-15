def isHYU(t):
    if t == 'H' or t == 'Y' or t == 'U':
        return 1
    return 0

n = int(input())
arr = list(input())
d,m = map(int,input().split())
now = 0
eng = 0
HYU = min(arr.count('H'), arr.count('Y'), arr.count('U'))

for i in range(n):
    text = arr[i]
    if not(isHYU(text)):
        now += 1
    elif now == 1:
        eng += d
        now = 0
    elif now != 0:
        eng += min((m + d), (now * d))
        now = 0
        
if now == 1:
    eng += d
elif now != 0:
    eng += min((m + d), (now * d))


if eng == 0:
    eng = 'Nalmeok'
if HYU == 0:
    HYU = 'I love HanYang University'
print(eng)
print(HYU)