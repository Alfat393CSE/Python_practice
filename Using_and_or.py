x = int(input("Enter a number: "))

if x > 0 and x % 2 == 0:
    print("Positive even number")
elif x > 0 and x % 2 != 0:
    print("Positive odd number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
