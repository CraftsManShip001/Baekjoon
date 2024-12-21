def sol(n):
    answer = 'V' * (n // 5) + 'I' * (n % 5)
    return answer
n = int(input())
print(sol(n))