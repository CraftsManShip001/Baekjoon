n = int(input())
idx = 1
for i in range(n,0,-1):
    print(' ' * (i-1),end = '')
    print('*' * idx)
    idx += 2