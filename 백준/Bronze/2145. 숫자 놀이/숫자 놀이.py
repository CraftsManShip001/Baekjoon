import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    if len(n) == 1:
        print(n)
        continue
    while 1 < len(n):
        n = str(sum(map(int, list(n))))
    print(n)
