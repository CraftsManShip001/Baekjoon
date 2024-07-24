n = int(input())
count = []
while n != 0:
    x = int(n / -2)
    if n == (-2 * x):
        n = x
        count.append(0)
    elif n == -2 * (x + 1):
        n = x + 1
        count.append(0)
    elif n == (-2 * x) + 1:
        n = x
        count.append(1)
    elif n == (-2 * (x + 1)) + 1:
        n = x + 1
        count.append(1)
if len(count) == 0:
    print(0)
else:
    for i in range(-1,(len(count) + 1) * -1,-1):
        print(count[i],end = '')