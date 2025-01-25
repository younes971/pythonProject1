import random

oikein_numero = random.randint(1, 10)

luku = int(input("syötä luku 1-10 väliltä: "))

if luku > oikein_numero:
    print("liian suuri arvaus.")
elif luku > 10:
    print("virheellinen syöte.")
elif luku < oikein_numero:
    print("liian pieni arvaus.")
elif luku < 1:
    print("virheellinen syöte.")

else:
    print("Arvasit oikein!")
