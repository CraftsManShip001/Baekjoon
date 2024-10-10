t = int(input())
for _ in range(t):
    n = input()
    if len(n) >= 6 and len(n) <= 9:
        print('yes')
    else:
        print('no')
