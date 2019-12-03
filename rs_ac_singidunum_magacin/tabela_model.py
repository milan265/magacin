from PySide2 import QtCore

class TabelaModel(QtCore.QAbstractTableModel):

    def __init__(self, hala):
        super().__init__()

        self._podaci = []
        self.ucitaj_podatke(hala)

    def rowCount(self, index):
        return len(self._podaci)

    def columnCount(self, index):
        return 6
    
    def data(self, index, role):
        element = self.get_element(index)
        if element is None:
            return None
        if role == QtCore.Qt.DisplayRole:
            return element
    
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if section == 0 and role == QtCore.Qt.DisplayRole:
                return "Naziv proizvoda"
            elif section == 1 and role == QtCore.Qt.DisplayRole:
                return "Rok upotrebe"
            elif section == 2 and role == QtCore.Qt.DisplayRole:
                return "Datum dodavanja"
            elif section == 3 and role == QtCore.Qt.DisplayRole:
                return "Datum isteka skladištenja"
            elif section == 4 and role == QtCore.Qt.DisplayRole:
                return "Temperatura proizvoda"
            elif section == 5 and role == QtCore.Qt.DisplayRole:
                return "Količina"

    def get_element(self, index: QtCore.QModelIndex):
        if index.isValid():
            element = self._podaci[index.row()][index.column()]
            if element:
                return element
        return None

    def ucitaj_podatke(self,hala):
        dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_proizvod.txt",'r')
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
            if naziv_hale == hala:
                s.append(naziv_proizvoda)
                s.append(rok_upotrebe)
                s.append(datum_dodavanja)
                d1 = QtCore.QDate.currentDate()
                d2 = QtCore.QDate.fromString(datum_isteka,"dd.MM.yyyy")
                if d1 > d2:
                    s.append("Istekao rok čuvanja")
                else:
                    s.append(datum_isteka)
                s.append(temperatura_proizvoda)
                s.append(int(kolicina))
                self._podaci.append(s)
        dat.close()

    """ def promeni_vrednost_kolicne(self, red, kolicina):
        try:
            self._podaci[red][5] = kolicina
            self.dataChanged()
        except:
            return False

    def ukloni_proizvod(self, red):
        self.beginRemoveRows(QtCore.QModelIndex(), red, red)
        del self._podaci[red]
        self.endRemoveRows() """