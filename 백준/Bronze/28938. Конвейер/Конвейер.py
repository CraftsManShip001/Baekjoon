N = int(input())
button = list(map(int, input().split()))
result = 0

for num in button:
  result += num

if result > 0:
  print("Right")
elif result == 0:
  print("Stay")
else:
  print("Left")