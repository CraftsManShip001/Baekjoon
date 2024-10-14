while True:
    m, a, b = map(int, input().split())
    if m == 0 and a == 0 and b == 0:
        break
    t = (m / a) - (m / b)
    s = round(t * 3600)
    h = s // 3600
    mi = (s % 3600) // 60
    sec = s % 60
    print("%d:%02d:%02d" % (h, mi, sec))