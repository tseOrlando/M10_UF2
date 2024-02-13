import random

try_ = 0
secr = random.randint(1, 100)
num  = ""

while int(num := input("num\n")) != secr:
    print("the number is " + ("lower than" if int(num) < secr else "bigger than") + " the number you gave")
    try_ += 1 #kek

print("secret " + str(secr) + "\n" +
      "tries " + str(try_))