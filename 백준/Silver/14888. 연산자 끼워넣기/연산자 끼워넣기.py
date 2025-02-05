import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
signs = list(map(int,input().split()))

maxnum = -1000000001
minnum = 1000000001

def find(idx,plus,minus,multi,divide,res):
    global maxnum,minnum
    if idx == n:
        maxnum = max(maxnum,res)
        minnum = min(minnum,res)
        return
    
    if plus:
        find(idx+1,plus-1,minus,multi,divide,res+nums[idx])
    if minus:
        find(idx+1,plus,minus-1,multi,divide,res-nums[idx])
    if multi:
        find(idx+1,plus,minus,multi-1,divide,res*nums[idx])
    if divide:
        find(idx+1,plus,minus,multi,divide-1,int(res/nums[idx]))

find(1,signs[0],signs[1],signs[2],signs[3],nums[0])

print(maxnum)
print(minnum)