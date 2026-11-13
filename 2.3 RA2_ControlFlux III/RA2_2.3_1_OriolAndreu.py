# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Genera una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari utilitzant range().
# Especificacions d'entrada: Un nombre enter introduït per l'usuari.

try:
    numero = int(input("Introdueix un nombre enter: "))
    
    # Si el nombre és positiu o zero, comptem cap amunt
    if numero >= 0:
        for i in range(numero + 1):
            print(i, end=" ")
    # Si el nombre és negatiu, comptem cap avall
    else:
        for i in range(0, numero - 1, -1):
            print(i, end=" ")
            
except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")
