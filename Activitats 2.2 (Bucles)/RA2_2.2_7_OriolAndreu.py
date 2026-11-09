# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Demana una cadena de text a l'usuari i la mostra invertida.
# Especificacions d'entrada: Una cadena de text introduïda per l'usuari.
text = input("Introdueix un text: ")

text_invertit = ""

for lletra in text:
    text_invertit = lletra + text_invertit  

print("El text invertit és:", text_invertit)
