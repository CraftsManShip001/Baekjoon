n = int(input())
seven = False
for i in range(len(str(n))):
    if str(n)[i] == '7':
        seven = True
        break
if seven == False and n % 7 != 0:
    print(0)
elif seven == False and n % 7 == 0:
    print(1)
elif seven == True and n % 7 != 0:
    print(2)
else:
    print(3)