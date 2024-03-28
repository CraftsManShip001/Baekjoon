from collections import deque
n,k = map(int,input().split())
arr = deque([i for i in range(1,n+1)])
an =  deque()
turn = 0
while True:
    turn += 1
    if turn == k:
        turn = 0
        an.append(arr.popleft())
    else:
        arr.append(arr.popleft())
    if len(arr) == 0:
        break
print('<',end = '')
for i in range(len(an)):
    if i == len(an) - 1:
        print(an[i],end = '')
    else:
        print('%d, '%an[i],end = '')
print('>')