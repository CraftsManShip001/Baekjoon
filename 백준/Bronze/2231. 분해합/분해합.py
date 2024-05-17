n = int(input())
num = 1
arr = []
check = False
while True:
    if num >= n:
        break
    h = str(num)
    a = num
    for i in range(len(h)):
        a += int(h[i])
    if a == n:
        check = True
        arr.append(num)
    num += 1
if check == False:
    print(0)
else:
    print(min(arr))