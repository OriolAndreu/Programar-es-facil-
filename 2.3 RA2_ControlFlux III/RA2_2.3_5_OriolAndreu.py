# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Demana un nombre enter positiu i imprimeix tots els nombres primers des de 2 fins a aquest nombre.
# Especificacions d'entrada: Un nombre enter positiu introduït per l'usuari.

try:
    n = int(input("Introdueix un nombre enter positiu: "))
    
    if n > 0:
        if n < 2:
            print("No hi ha nombres primers menors que 2.")
        else:
            print("Nombres primers des de 2 fins a", n, ":")
            
            # Primer bucle: recorre cada número des de 2 fins a n
            for num in range(2, n + 1):
                es_primer = True
                
                # Segon bucle: comprova si 'num' es pot dividir per algun número anterior
                for divisor in range(2, num):
                    if num % divisor == 0:
                        es_primer = False
                        
                # Si després de provar tots els divisors continua sent True, l'imprimim
                if es_primer:
                    print(num)
    else:
        print("Error: El nombre ha de ser positiu (més gran que 0).")

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")