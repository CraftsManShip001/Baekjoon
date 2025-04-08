a,b=map(int,input().split())
m=(str(a//b)+".")
a=(a%b)*10
for i in range(1000):
    m+=str(a//b)
    a=(a%b)*10
print(m)