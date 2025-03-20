class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0,kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettumatka = 0


    def kiihdyta(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0


auto = Auto("ABC-123", 142)

print(f"rekisteritunnus: {auto.rekisteritunnus}")
print(f"huippunopeus: {auto.huippunopeus} km/h")
print(f"kuljettumatka: {auto.kuljettumatka} km")
print(f"tämänhetkinennopeus: {auto.tämänhetkinen_nopeus} km/h")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"auton nopeus kiihdyksen jälkeen: {auto.tämänhetkinen_nopeus} km/h")

auto.kiihdyta(-200)
print(f"auton nopeus jarrutuksen jälkeen: {auto.tämänhetkinen_nopeus} km/h")

