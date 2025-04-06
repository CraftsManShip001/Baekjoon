import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()

print(1) if p in s else print(0)