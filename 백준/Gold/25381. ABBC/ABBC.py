arr = list(input())
b_cnt = arr.count('B')
a = 0
b = 0
abbc_cnt = 0
for i in arr:
    if i == 'A':
        a += 1
    elif i == 'B' and a > 0:
        abbc_cnt += 1
        a -= 1
for i in arr:
    if i == 'B':
        b += 1
    elif i == 'C' and b > 0:
        abbc_cnt += 1
        b -= 1
print(min(abbc_cnt,b_cnt))