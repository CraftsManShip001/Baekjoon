a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
app = (a * 3) + (b * 2) + c
ban = (d * 3) + (e * 2) + f
if app > ban:
    print('A')
elif ban > app:
    print('B')
else:
    print('T')