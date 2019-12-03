from PySide2 import QtCore

class TabelaIstorija(QtCore.QAbstractTableModel):

    def __init__(self):
        super().__init__()

        self._podaci = []
        self.ucitaj_podatke()

    def rowCount(self, index):
        return len(self._podaci)

    def columnCount(self, index):
        return 9
    
    def data(self, index, role):
        element = self.get_element(index)
        if element is None:
            return None
        if role == QtCore.Qt.DisplayRole:
            return element
    
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if section == 0 and role == QtCore.Qt.DisplayRole:
                return "Naziv hale"
            elif section == 1 and role == QtCore.Qt.DisplayRole:
                return "Naziv proizvoda"
            elif section == 2 and role == QtCore.Qt.DisplayRole:
                return "Rok upotrebe"
            elif section == 3 and role == QtCore.Qt.DisplayRole:
                return "Datum dodavanja"
            elif section == 4 and role == QtCore.Qt.DisplayRole:
                return "Datum isteka skladištenja"
            elif section == 5 and role == QtCore.Qt.DisplayRole:
                return "Temperatura proizvoda"
            elif section == 6 and role == QtCore.Qt.DisplayRole:
                return "Temperatura hale"
            elif section == 7 and role == QtCore.Qt.DisplayRole:
                return "Količina"

    def get_element(self, index: QtCore.QModelIndex):
        if index.isValid():
            element = self._podaci[index.row()][index.column()]
            if element:
                return element
        return None

    def ucitaj_podatke(self):
        dat = open("./plugins/rs_ac_singidunum_magacin/podaci/istorija.txt",'r')
        while True:
            s = []
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
            s.append(naziv_hale)
            s.append(naziv_proizvoda)
            s.append(rok_upotrebe)
            s.append(datum_dodavanja)
            s.append(datum_isteka)
            s.append(temperatura_proizvoda)
            if temperatura_hale == "1":
                s.append("od -10C do 0C")
            elif temperatura_hale == "2":
                s.append("od 1C do 18C")
            else:
                s.append("od 19C do 25C")
            s.append(kolicina)
            self._podaci.append(s)
        dat.close()