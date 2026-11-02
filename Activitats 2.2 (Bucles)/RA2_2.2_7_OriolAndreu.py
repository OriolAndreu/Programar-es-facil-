# Demanem el text a l'usuari (les cadenes de text no necessiten 'int')
text = input("Introdueix un text: ")

text_invertit = ""

# El bucle 'for' recorre el text lletra per lletra automàticament
for lletra in text:
    text_invertit = lletra + text_invertit  

print("El text invertit és:", text_invertit)
