import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) 

def find(idx):
    global visit
    visit[idx] = 1
    for i in arr[idx]:
        if visit[i]==-1:
            visit[idx]+=find(i)
    return visit[idx]

n,r,q=map(int,input().split(' '))
visit = [-1 for _ in range(n+1)]
arr = [[]for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split(' '))
    arr[a].append(b)
    arr[b].append(a)
find(r)
for _ in range(q):
    print(visit[int(input())])