nimi = input("anna sinun nimi: ")
print("Tervetuloa, "+ nimi + "!")



import math

sade = float(input("anna ympyrän sade: "))
Ympärysmitta = math.pi * sade * sade
print(f"ympyärän_pintaala: {Ympärysmitta} ")



suorakulmion_kanta = float(input("anna suorakulmion kanta: "))
suorakulmion_korkeus = float(input("anna suorakulmiun korkeus: "))

pintaala = suorakulmion_kanta * suorakulmion_korkeus
suorakulmion_piiri = 2 * (suorakulmion_kanta + suorakulmion_korkeus)
print(f"pinta_ala: {suorakulmion_piiri} ")



luku1 = int(input("anna luku1: "))
luku2 = int(input("anna luku2: "))
luku3 = int(input("anna luku3: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f"summa: {summa} ")
print(f"tulo: {tulo} ")
print(f"keskiarvo: {keskiarvo} ")



Leiviskät = float(input("anna leiviskät: "))
Nauloja = float(input("anna nauloja: "))
Luodit = float(input("annna luodit: "))


grammaa_per_luoti = 13.3
kokonaisluoteja_per_naula = 32
kokonaisnauloja_per_leiviska = 20


kokonaisgrammat = 13.3 * 32*13.3 + 32*20

kilogrammat = int(kokonaisgrammat // 1000)
grammat = int(kokonaisgrammat % 1000)

print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa")


import random

kolmenumero_koodi = "".join(str(random.randint(0,9)) for _ in range (3))
nelinumero_koodi = "".join(str(random.randint(1,6)) for _ in range (4))

print(f"kolmenumero_koodi: {kolmenumero_koodi}")
print(f"nelinumero_koodi: {nelinumero_koodi}")




