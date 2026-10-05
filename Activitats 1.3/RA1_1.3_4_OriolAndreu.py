# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

#Error:
#input() retorna text (str). No es pot sumar directament un número a una cadena.
#Programa corregit:
edat = int(input("Quants anys tens? "))
edat_futura = edat + 5
print(edat_futura)