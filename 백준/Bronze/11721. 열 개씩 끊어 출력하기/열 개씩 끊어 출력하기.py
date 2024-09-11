n = input()
for i in range(10,len(n),10):
    print(n[i-10:i])
try:
    print(n[i:])
except:
    print(n)