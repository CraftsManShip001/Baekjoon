n = int(input())
arr = list(input())
a = arr.count('A')
b = arr.count('B')
if a > b:
    print('A')
elif a < b:
    print('B') 
else:
    print('Tie')