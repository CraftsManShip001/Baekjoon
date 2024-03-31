n = int(input())
def find():
    for i in range(n // 3 + 2):
        for j in range(n // 5 + 2):
            if i * 3 + j * 5 == n:
                return i + j
    return -1
print(find())