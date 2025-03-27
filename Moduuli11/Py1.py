class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

        def tulosta_tiedot(self):
            pass

class Kirja (Julkaisu):

            def __init__(self,nimi, kirjoittaja, sivumaara):
                self.kirjoittaja = kirjoittaja
                self.sivumaara = sivumaara
                super().__init__(kirjoittaja, sivumaara)

            def tulosta_tiedot(self):
                super().tulosta_tiedot()
                print(f"Kirja: {self.kirjoittaja}, sivumaara:{self.sivumaara}")

class Lehti (Julkaisu):

            def __init__(self,nimi, paatoimittaja):
                self.paatoimittaja = paatoimittaja
                super().__init__(paatoimittaja)

            def tulosta_tiedot(self):
                super().tulosta_tiedot()
                print(f"Lehti: {self.paatoimittaja}")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Hytti_nro_6","Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_nro_6.tulosta_tiedot()





