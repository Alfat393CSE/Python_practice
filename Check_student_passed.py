marks = int(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 79:
    print("A")
elif marks >= 60 and marks <= 69:
    print("B")
elif marks >= 50 and marks <= 59:
    print("C")
else:
    print("Fail")
