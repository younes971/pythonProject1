oikea_kättäjä_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
maksimi_yritykset = 5

while yritykset < maksimi_yritykset:
    käyttäjä_tunnus = input("syötä käyttäjätunnus: ")
    salasana = input("syötä salasana: ")

if käyttäjä_tunnus == oikea_kättäjä_tunnus and salasana == oikea_salasana:
    print("Tervetuloa.")

else:
    print("Väärä tunnus tai salasana.")
    yritykset = yritykset + 1
    print("Pääsy evätty.")


