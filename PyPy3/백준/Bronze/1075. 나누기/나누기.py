n = input()
f = int(input())
start = int(n[:-2] + '00')
end = int(n[:-2] + '99')
for i in range(start, end):
    if i % f == 0:
        a = str(i)
        print(a[-2:])
        break