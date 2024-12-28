t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

max_time = 3 * t1 + 20 * e1 + 120 * f1
mel_time = 3 * t2 + 20 * e2 + 120 * f2

if max_time > mel_time:
    print("Max")
elif max_time < mel_time:
    print("Mel")
else:
    print("Draw")