try:
    while True :
        n = input()
        for i in range(len(n)) :
            if n[i] == 'e' : print("i", end = "")
            elif n[i] == 'E' : print("I", end = "")
            elif n[i] == 'I' : print("E", end = "")
            elif n[i] == 'i' : print("e", end = "")
            else : print(n[i], end = "")
        print()
except:
    exit(0)