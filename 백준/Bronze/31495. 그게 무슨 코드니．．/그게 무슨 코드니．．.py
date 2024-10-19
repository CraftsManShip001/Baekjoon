n = list(input())
if n[0] == '"' and n[-1] == '"' and len(n) != 2:
    flag = 0
    for i in range(1,len(n)-1):
        if n[i] != ' ':
            flag = 1
        print(n[i],end = '')
    if flag == 0:
        print('CE')
else:
    print('CE')