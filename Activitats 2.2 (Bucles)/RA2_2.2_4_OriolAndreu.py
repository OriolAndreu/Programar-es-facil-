import random
a = random.randint(1, 100)
while True:
    b = int(input("Introdueix un número del 1-100: "))
    if b == a:
        print("Has encertat!")
        break
    if a > b:
        print("El número és més gran")

    if a < b:
        print("El número és més petit")
