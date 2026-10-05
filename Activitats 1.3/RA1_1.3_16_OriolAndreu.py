# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa elimina els espais del principi i del final d'una frase.

frase = input("Frase: ")

frase_neta = frase.strip()

print("[" + frase_neta + "]")