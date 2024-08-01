import sys
text = list(sys.stdin.readline().strip())
boom = list(sys.stdin.readline().strip())
n = len(boom)
stack = []
for i in text:
    stack.append(i)
    if stack[len(stack)-n:len(stack)] == boom:
        for j in range(n):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")