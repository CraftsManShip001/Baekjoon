def sol(s):
    s=s.lower()
    s= list(s.split())
    answer = 'Y'
    for i in range(1, len(s)):
        if s[i][0] != s[i-1][0]:
            answer = 'N'
    return answer
while True:
    s = input()
    if s == '*':
        break
    print(sol(s))