# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa mostra una frase en majúscules, minúscules i el nombre de caràcters.

frase = input("Frase: ")

print("Original: " + frase)
print("Majúscules: " + frase.upper())
print("Minúscules: " + frase.lower())
print("Caràcters: " + str(len(frase)))