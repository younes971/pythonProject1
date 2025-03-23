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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissien_lkm = [Hissi (alin_kerros, ylin_kerros) for i in range (hissien_lkm)]

    def aja_hissi(self,hissin_numero, kohde_kerros):
        if 0 <= hissin_numero > len(self.hissien_lkm):
            print(f"ajetaan hissi {hissin_numero} kerrokseen {kohde_kerros}")

        else:
            print("Virhellinen syötö.")