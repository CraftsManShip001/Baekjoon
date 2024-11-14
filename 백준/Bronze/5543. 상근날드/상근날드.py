ham = []
drk = []
for _ in range(3):
    n = int(input())
    ham.append(n)
for _ in range(2):
    n = int(input())
    drk.append(n)
print(min(ham) + min(drk) - 50)