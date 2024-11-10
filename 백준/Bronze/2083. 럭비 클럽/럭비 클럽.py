while True:
    name,age,w = input().split()
    if name == '#' and age == '0' and w == '0':
        break
    print(name,end = ' ')
    if int(age) > 17 or int(w) >= 80:
        print('Senior')
    else:
        print('Junior')