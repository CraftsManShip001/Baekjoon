a = int(input())
b = int(input())
n = b - a

if n <= 0:
    print("Congratulations, you are within the speed limit!")
elif n >= 31:
    print("You are speeding and your fine is ${}.".format(500))
elif n >= 1 and n <= 20:
    print("You are speeding and your fine is ${}.".format(100))
elif n >= 21 and n <= 30:
    print("You are speeding and your fine is ${}.".format(270))