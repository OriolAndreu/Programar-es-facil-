numero = int (input("Introdueix un número enter: "))
for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} no és primer")
        break
else:
    print(f"{numero} és primer")