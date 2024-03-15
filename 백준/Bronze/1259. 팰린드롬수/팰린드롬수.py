while True:
    a = list(input())
    if a == ['0']:
        break
    b = a[:]
    a.reverse()
    if a == b:
        print('yes')
    else:
        print('no')