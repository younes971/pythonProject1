import random

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

    def kulje(self, tunnit):
         self.kuljettumatka += self.tämänhetkinen_nopeus * tunnit

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i}", huippunopeus))

    kilpailu_käynissä = True
    while kilpailu_käynissä:
        for auto in autot:
            auto.kiihdyta(random.randint (-10 , 15))
            auto.kulje(1)
            if auto.kuljettumatka >= 10000:
                kilpailu_käynissä = False
                break

        print(f"{auto.rekisteritunnus:<10},{auto.tämänhetkinen_nopeus:<15}, {huippunopeus:<15},{auto.kuljettumatka:<10}")

