n = int(input())
idx = 1
for j in range(n,0,-1):
    print(' ' * (j-1),end = '')
    print('*' * idx)
    idx += 2
idx = (1 + (2 * (n-2)))
for i in range(n-1,0,-1):
    print(' ' * (n-i),end = '')
    print('*' * idx)
    idx -= 2