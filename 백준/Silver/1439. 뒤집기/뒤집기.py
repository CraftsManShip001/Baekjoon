s = input()
n1 = s[:].split('0')
n2 = s[:].split('1')
print(min(len(n1) - n1.count(''),len(n2)-n2.count('')))