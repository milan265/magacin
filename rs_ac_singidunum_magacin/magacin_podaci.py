#immutable
from .hala import Hala

class MagacinPodaci():

    def __init__(self):
        self._magacin_lista = []
        self.ucitaj_podatke()

    @property
    def magacin_lista(self):
        return self._magacin_lista

    def ucitaj_podatke(self):
        dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_podaci.txt",'r')
        while True:
            naziv = dat.read(10).strip()
            if naziv=="":
                break
            kapacitet = dat.read(5).strip()
            broj_zauzetih_mesta = dat.read(5).strip()
            temp = dat.read(3).strip()
            dat.read(1)
            self._magacin_lista.append(Hala(naziv, int(kapacitet), int(broj_zauzetih_mesta), int(temp)))
        dat.close()    
    
    def nadji_halu(self, naziv):
        for i in self._magacin_lista:
            if i.naziv == naziv:
                return i