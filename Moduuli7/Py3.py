lentoasemat = set()

koodit = {}

A = "syötä uusi lentoasemat"
B = "hakea jo syötetyn lentoaseman tiedot"
C = "lopeta"

käyttäjän_valinta = input("valitse A tai B tai C: ")

if käyttäjän_valinta == A:
    ICAO = input("anna lentoaseman ICAO-koodi: ")
    nimi = input("anna lentoaseman nimi: ")
    print(f"lentoasema {nimi} ICAO: {ICAO}")

elif käyttäjän_valinta == B:
    ICAO = input("anna ICAO koodi: ")
    if ICAO in koodit:
        print(f"lentoasema on ICAO-koodi: {ICAO}")

elif käyttäjän_valinta== C:
    print("lopeta toiminta")


else:
    print("virheellinen valinta!")


