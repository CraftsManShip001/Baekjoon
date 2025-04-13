n = int(input())
idx = 1
while idx * idx <= n:
    idx += 1
print("The largest square has side length " + str(idx - 1) + ".")