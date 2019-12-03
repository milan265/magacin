#immutable
from .proizvod import Proizvod

class ProizvodPodaci():

    def __init__(self):
        self._proizvod_lista = []
        self.ucitaj_podatke()

    @property
    def proizvod_lista(self):
        return self._proizvod_lista

    def ucitaj_podatke(self):
        dat = open("./plugins/rs_ac_singidunum_magacin/podaci/proizvod_podaci.txt",'r')
        while True:
            naziv = dat.read(15).strip()
            if naziv=="":
                break
            rok_upotrebe = dat.read(13).strip()
            temperatura = dat.read(3).strip()
            kolicina = dat.read(5).strip()
            dat.read(1)
            self._proizvod_lista.append(Proizvod(naziv, rok_upotrebe, int(temperatura), int(kolicina)))
        dat.close()
    def nadji_proizvod(self, naziv, rok_upotrebe):
        for i in self._proizvod_lista:
            if i.naziv == naziv and i.rok_upotrebe==rok_upotrebe:
                return i   