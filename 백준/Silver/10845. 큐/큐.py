import sys
stack = []
for i in range(int(input())):
  arr = sys.stdin.readline().strip().split()
  if arr[0] == 'push':
    stack.append(arr[1])
  elif arr[0] == 'pop':
    if len(stack) != 0:
      print(stack.pop(0))
    else:
      print(-1)
  elif arr[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif arr[0] == 'size':
    print(len(stack))
  elif arr[0] == 'front':
    if len(stack) != 0:
      print(stack[0])
    else:
      print(-1)
  elif arr[0] == 'back':
    if len(stack) != 0:
      print(stack[-1])
    else:
      print(-1)