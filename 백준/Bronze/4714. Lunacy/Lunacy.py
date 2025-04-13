while True:
    w = float(input())
    if w == -1.0:
        break
    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (w,w * 0.167))
