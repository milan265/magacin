class Hala():
    def __init__(self, naziv, kapacitet:int, broj_zauzetih_mesta:int, temperatura:int):
    #vrednost za temp moze biti 1,2,3
    #1 je oznaka za temperaturu od -10C do 0C
    #2 je oznaka za temperaturu od 1C do 18C
    #3 je oznaka za temperaturu od 19C do 25C
        self._naziv = naziv
        self._kapacitet = kapacitet
        self._broj_zauzetih_mesta = broj_zauzetih_mesta
        self._temperatura = temperatura

    @property
    def naziv(self):
        return self._naziv
    @naziv.setter
    def naziv(self, vrednost):
        self._naziv = vrednost
        
    @property
    def kapacitet(self):
        return self._kapacitet
    @kapacitet.setter
    def kapacitet(self, vrednost):
        self._kapacitet = vrednost
    
    @property
    def broj_zauzetih_mesta(self):
        return self._broj_zauzetih_mesta
    @broj_zauzetih_mesta.setter
    def broj_zauzetih_mesta(self, vrednost):
        self._broj_zauzetih_mesta = vrednost

    @property
    def temperatura(self):
        return self._temperatura
    @temperatura.setter
    def temperatura(self, vrednost):
        self._temperatura = vrednost