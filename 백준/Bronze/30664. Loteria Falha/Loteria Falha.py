while True:
    try:
        number = int(input().strip())
        if number == 0:
            break
        if number % 42 == 0:
            print("PREMIADO")
        else:
            print("TENTE NOVAMENTE")
    except EOFError:
        break
