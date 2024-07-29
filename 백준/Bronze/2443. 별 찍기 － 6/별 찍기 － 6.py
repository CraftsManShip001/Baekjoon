n = int(input())
idx = (1 + (2 * (n-1)))
for i in range(n,0,-1):
    print(' ' * (n-i),end = '')
    print('*' * idx)
    idx -= 2