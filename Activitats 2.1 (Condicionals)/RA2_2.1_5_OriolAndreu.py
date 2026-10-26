# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 26/10/2026
# Descripció: Calcula si l'usuari és major d'edat comparant de manera precisa el dia, mes i any de naixement amb la data actual.
# Especificacions d'entrada: Tres valors sencers (int) per separat: dia, mes i any.

# Comentari clau: S'importa el mòdul extern 'date' per poder extreure el dia, mes i any actuals del sistema de l'ordinador.
from datetime import date

dia = int(input("Quin dia vas néixer? "))
mes = int(input("Quin mes vas néixer? "))
any = int(input("Quin any vas néixer? "))
data_avui = date.today()
anys = data_avui.year - any
if (anys > 18):
    print("Ets major d'edat.")
if (anys < 18):
    print("Ets menor d'edat.")
if (anys == 18):
    if (mes < data_avui.month):
        print("Ets major d'edat.")
    if (mes > data_avui.month):
        print("Ets menor d'edat.")
    if (mes == data_avui.month):
        if (dia <= data_avui.day):
            print("Ets major d'edat.")
        if (dia > data_avui.day):
            print("Ets menor d'edat.")
        if (dia == data_avui.day):
            print("Felicitats!")
