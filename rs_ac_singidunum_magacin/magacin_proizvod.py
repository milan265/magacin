class MagacinProizvod():
    def __init__(self, naziv_hale, naziv_proizvoda, rok_upotrebe, datum_dodavanja, datum_isteka, temperatura_proizvoda, temperatura_hale, kolicina):
        self._naziv_hale = naziv_hale
        self._naziv_proizvoda = naziv_proizvoda
        self._rok_upotrebe = rok_upotrebe
        self._datum_dodavanja = datum_dodavanja
        self._datum_isteka = datum_isteka
        self._temperatura_proizvoda = temperatura_proizvoda
        self._temperatura_hale = temperatura_hale
        self._kolicina = kolicina

    @property
    def naziv_hale(self):
        return self._naziv_hale
    @naziv_hale.setter
    def naziv_hale(self, vrednost):
        self._naziv_hale = vrednost

    @property
    def naziv_proizvoda(self):
        return self._naziv_proizvoda
    @naziv_proizvoda.setter
    def naziv_proizvoda(self, vrednost):
        self._naziv_proizvoda = vrednost
    
    @property
    def rok_upotrebe(self):
        return self._rok_upotrebe
    @rok_upotrebe.setter
    def rok_upotrebe(self, vrednost):
        self._rok_upotrebe = vrednost
    
    @property
    def datum_dodavanja(self):
        return self._datum_dodavanja
    @datum_dodavanja.setter
    def datum_dodavanja(self, vrednost):
        self._datum_dodavanja = vrednost
    
    @property
    def datum_isteka(self):
        return self._datum_isteka
    @datum_isteka.setter
    def datum_isteka(self, vrednost):
        self._datum_isteka = vrednost
    
    @property
    def temperatura_proizvoda(self):
        return self._temperatura_proizvoda
    @temperatura_proizvoda.setter
    def temperatura_proizvoda(self, vrednost):
        self._temperatura_proizvoda = vrednost
    
    @property
    def temperatura_hale(self):
        return self._temperatura_hale
    @temperatura_hale.setter
    def temperatura_hale(self, vrednost):
        self._temperatura_hale = vrednost
    
    @property
    def kolicina(self):
        return self._kolicina
    @kolicina.setter
    def kolicina(self, vrednost):
        self._kolicina = vrednost