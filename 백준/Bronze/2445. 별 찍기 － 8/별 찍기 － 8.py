n = int(input())
idx = (n * 2) - 2
num = 1
m = 1
l = -2
for i in range((n * 2)-1):
    if num == (n+1):
        num = (n-1)
        m = -1
        l = 2
        idx = 2
    print('*' * num,end = "")
    print(' ' * idx,end = '')
    print('*' * num)
    num += m
    idx += l