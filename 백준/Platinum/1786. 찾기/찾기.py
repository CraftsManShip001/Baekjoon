def kmp_pattern_search(text, pattern):
    n, m = len(text), len(pattern)
    pi = [0] * m
    result = []

    # KMP 테이블 생성
    for i in range(1, m):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    # KMP 검색
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                result.append(i - m + 2)
                j = pi[j]
            else:
                j += 1

    return result

text = input()
pattern = input()

result = kmp_pattern_search(text, pattern)
print(len(result))
print(*result)