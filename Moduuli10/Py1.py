class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros +=1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -=1
            print("Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self,kohde_kerros):
        if kohde_kerros > self.nykyinen_kerros:
            print("siirretään hissi ylös")
        else:
          print("Virhe: kohdekerros ei ole salittu.")


testiHissi = Hissi(1,7)
print(f"Siirretään hissi viidenteen kerrokseen.")
