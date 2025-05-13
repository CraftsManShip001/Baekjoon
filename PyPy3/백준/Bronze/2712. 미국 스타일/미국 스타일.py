t = int(input())
arr = {'kg': ['lb', 2.2046], 'lb': ['kg', 0.4536], 'l': ['g', 0.2642], 'g': ['l', 3.7854]}
ans = ""
for i in range(t):
    num, unit = input().split() 
    ans += str('{:.4f}'.format(round(float(num)*arr[unit][1], 4))) + " " + arr[unit][0] + "\n"
print(ans)