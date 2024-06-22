import random
x = int(input("Number A"))
y = int(input("Number B"))
count = 0
number = random.randint(x, y)

z = int(input("Guess the number"))
count = count + 1
while z != number:
    print("Wrong, try again!")
    z = int(input("Guess the number"))
    count = count + 1

print(number, "is correct! It took you", count, "tries!")