n = int(input())
count = 0
for i in range(1,n + 1):
    num = str(i)
    if len(num) == 3:
        if int(num[0])-int(num[1]) == int(num[1])-int(num[2]):
            count += 1
    elif len(num) != 4:
        count += 1
print(count)