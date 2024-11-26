import sys

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    print(sum([i for i in range(1, N + 1)]))