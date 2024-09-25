n,m = map(int,input().split())
if m < 3:
    print('NEWBIE!')
elif n >= m:
    print('OLDBIE!')
else:
    print('TLE!')