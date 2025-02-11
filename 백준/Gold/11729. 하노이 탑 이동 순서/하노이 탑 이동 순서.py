def 하노이탑(num, start, end):
    if num == 1:
        print(start, end)
        return
    else:
        하노이탑(num-1, start, 6-start-end)
        print(start, end)
        하노이탑(num-1, 6-start-end, end)
n = int(input())
print(2**n -1)
하노이탑(n, 1, 3)