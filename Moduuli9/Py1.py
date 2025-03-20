class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0,kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettumatka = 0


auto = Auto("ABC-123", 142)

print(f"rekisteritunnus: {auto.rekisteritunnus}")
print(f"huippunopeus: {auto.huippunopeus} km/h")
print(f"kuljettumatka: {auto.kuljettumatka} km")
print(f"tämänhetkinennopeus: {auto.tämänhetkinen_nopeus} km/h")

