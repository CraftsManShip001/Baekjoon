def find(x,y,d):
    while 1:
        if x == (n-1) and y == 1:
            res = True
            break
        elif x >= n or y > 1:
            res = False
            break
        if y == 0:
            if top[x] == 'I':
                if d == 'left':
                    x += 1
                else:
                    res = False
                    break
            else:
                if d == 'left':
                    y = 1
                    d = 'bottom'
                elif d == 'top':
                    x += 1
                    y = 0
                    d = 'left'
                else:
                    res = False
                    break
        else:
            if bot[x] == 'I':
                if d == 'left':
                    x += 1
                else:
                    res = 0
                    break
            else:
                if d == 'bottom':
                    x += 1
                    y = 1
                    d = 'left'
                elif d == 'left':
                    y = 0
                    d = 'top'
                else:
                    res = 0
                    break
    return res

n = int(input())
top = list(input())
bot = list(input())
if find(1,0,'left') or find(0,1,'bottom'):
    print('YES')
else:
    print('NO')