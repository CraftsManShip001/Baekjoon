f_map = list(map(int, input().split()))
f_inv = [0] * 10
for i in range(10):
    f_inv[f_map[i]] = i
a, b = input().split()
a = int(''.join(str(f_inv[int(x)]) for x in a))
b = int(''.join(str(f_inv[int(x)]) for x in b))
c = str(a + b)
print(''.join(str(f_map[int(x)]) for x in c))