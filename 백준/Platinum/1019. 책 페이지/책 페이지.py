n = int(input())
x = 1
arr = [0 for _ in range(10)]
def every_up():
    for l in range(n+1):
        arr[l] += x
    return
while True:
    while n % 10 != 9:
        for i in str(n):
            arr[int(i)] += x
        n -= 1
    if n < 10:
        every_up()
        arr[0] -= x
        break
    else:
        num = ((n // 10) + 1) * x
        for i in range(10):
            arr[i] += num
        arr[0] -= x
    x *= 10
    n = n // 10
print(*arr)