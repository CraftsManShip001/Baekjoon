count = 0
while (1) :
    try :
        text = input()
        count += 1
    except EOFError :
        break;     
print(count)