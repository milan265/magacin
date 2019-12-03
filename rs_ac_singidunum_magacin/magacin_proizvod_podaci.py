#immutable
from .magacin_proizvod import MagacinProizvod

class MagacinProizvodPodaci():

    def __init__(self):
        self._magacin_proizvod_lista = []
        self.ucitaj_podatke()

    @property
    def magacin_proizvod_lista(self):
        return self._magacin_proizvod_lista

    def ucitaj_podatke(self):
        dat = open("./plugins/rs_ac_singidunum_magacin/podaci/istorija.txt",'r')
        while True:
            naziv_hale = dat.read(10).strip()
            if naziv_hale=="":
                break
            naziv_proizvoda = dat.read(15).strip()
            rok_upotrebe = dat.read(11).strip()
            datum_dodavanja = dat.read(11).strip()
            datum_isteka = dat.read(11).strip()
            temperatura_proizvoda = dat.read(4).strip()
            temperatura_hale = dat.read(2).strip()
            kolicina = dat.read(4).strip()
            dat.read(1)
            self._magacin_proizvod_lista.append(MagacinProizvod(naziv_hale,naziv_proizvoda,rok_upotrebe,datum_dodavanja,datum_isteka,temperatura_proizvoda,temperatura_hale,int(kolicina)))
        dat.close()
    def nadji_magacin_proizvod(self, naziv_hale, naziv_proizvoda , rok_upotrebe):
        for i in self._magacin_proizvod_lista:
            if i.naziv_hale == naziv_hale and i.naziv_proizvoda==naziv_proizvoda and i.rok_upotrebe==rok_upotrebe:
                return i   