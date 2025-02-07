kuukaudet = ("tammikku","helmikuu","maaliskuu","huuhtikuu","toukokuu","kesäkuu","heinäkuu","elokuu","syyskuu","lokakuu","marraskuu","joulukuu")


talvi = ("joulukuu","tammikuu","helmikkuu")
kevät = ("maaliskuu","huuhtikuu","toukuokuu")
kesä = ("kesäkuu","heinäkuu","elokuu")
syksy = ("syyskuu","lokakuu","marraskuu")


kuukauden_numero = int(input("anna kuukauden numero (1-12): "))

if 1 <= kuukauden_numero <= 12:
    kuukausi = kuukaudet[kuukauden_numero-1]

    if kuukausi in talvi:
        vuodenaika = "talvi"
    elif kuukausi in kevät:
        vuodenaika = "kevät"
    elif kuukausi in kesä:
        vuodenaika = "kesä"
    elif kuukausi in syksy:
        vuodenaika = "syksy"

    print(f"{kuukauden_numero}. kuukausi {kuukausi} kuuluu vuodenaikaan {vuodenaika}")

else:
    print("virheellinen numero!")

