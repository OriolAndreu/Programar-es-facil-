# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0
#
# Descripció: Què fa el programa
# Especificacions d'entrada: Dades que rep el programa
num1 = input("Introdueix el primer número: ")
operacio = input("Introdueix l'operació (+, -, *, /): ")
num2 = input("Introdueix el segon número: ")

# Construïm la loperació com un text (ex: "5 + 3") i l'avaluem
expressio = num1 + " " + operacio + " " + num2
resultat = eval(expressio)

print("El resultat és: " + str(resultat))
