import random

silmälukujen_summma = 0

arpojen_määrä = int(input("anna arpakuutioiden lukumäärä: "))

for _ in range (arpojen_määrä):
    heitto = random.randint(1,6)
    silmälukujen_summma += heitto
    print(f"silmälukujen summan, summa on {silmälukujen_summma}.")
