# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa neteja un nom d'usuari i mostra la seva longitud.

usuari = input("Nom d'usuari: ")

usuari = usuari.strip().lower()

print("Usuari: " + usuari)
print("Caràcters: " + str(len(usuari)))