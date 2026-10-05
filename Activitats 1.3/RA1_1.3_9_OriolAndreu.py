# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa calcula l'import d'una compra, l'IVA i el preu total.

preu = float(input("Preu sense IVA: "))
unitats = int(input("Nombre d'unitats: "))

subtotal = preu * unitats
iva = subtotal * 0.21
total = subtotal + iva

print("Import sense IVA: " + str(subtotal))
print("IVA: " + str(iva))
print("Total amb IVA: " + str(total))