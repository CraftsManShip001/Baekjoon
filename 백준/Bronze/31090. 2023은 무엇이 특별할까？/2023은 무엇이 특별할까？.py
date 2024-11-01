t = int(input())
for i in range(t):
    n = int(input())
    if (n+1) % int(str(n)[2:]) == 0:
        print('Good')
    else:
        print('Bye')