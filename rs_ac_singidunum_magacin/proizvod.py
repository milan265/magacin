class Proizvod():
    def __init__(self, naziv, rok_upotrebe, temperatura, kolicina):
        self._naziv = naziv
        self._rok_upotrebe = rok_upotrebe
        self._temperatura = temperatura
        self._kolicina = kolicina

    @property
    def naziv(self):
        return self._naziv
    @naziv.setter
    def naziv(self, vrednost):
        self._naziv = vrednost

    @property
    def rok_upotrebe(self):
        return self._rok_upotrebe
    @rok_upotrebe.setter
    def rok_upotrebe(self, vrednost):
        self._rok_upotrebe = vrednost
    @property
    def temperatura(self):
        return self._temperatura
    @temperatura.setter
    def temperatura(self, vrednost):
        self._temperatura = vrednost
    @property
    def kolicina(self):
        return self._kolicina
    @kolicina.setter
    def kolicina(self, vrednost):
        self._kolicina = vrednost