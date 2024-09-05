import random

x = int(input("Enter lower boundary "))
y = int(input("Enter higher boundary "))
z = ""
count = 0
number = random.randint(x, y)

while z != number:
    if z == "":
        z = int(input("Guess the number "))
        count = count + 1
    elif z > number:
        print("Lower!")
        z = int(input("Guess again "))
        count = count + 1
    elif z < number:
        print("Higher!")
        z = int(input("Guess again "))
        count = count + 1

print(number, "is correct! It took you", count, "tries!")