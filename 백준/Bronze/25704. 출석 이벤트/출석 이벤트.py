n = int(input())
price = int(input())

arr = [500,10,2000,4]
res = [price]
if n < 21:
    idx = n // 5
else:
    idx = 4
for i in range(idx):
    if i % 2:
        num = price - (price // arr[i])
    else:
        num = price - arr[i]
    if num < 0 :
        num = 0
    res.append(num)
print(min(res))