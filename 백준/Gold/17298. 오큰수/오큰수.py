import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
an = []
stack = [-1] * n
arr.reverse()
for i in range(n):
    num = arr[i]
    while an:
        if an[-1] > num:
            stack[i] = an[-1]
            break
        else:
            an.pop()
    an.append(num)
stack.reverse()
for l in stack:
    print(l,end = ' ')