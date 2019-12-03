from PySide2 import QtCore

class TabelaSveHale(QtCore.QAbstractTableModel):

    def __init__(self):
        super().__init__()

        self._podaci = []
        self.ucitaj_podatke()

    def rowCount(self, index):
        return len(self._podaci)

    def columnCount(self, index):
        return 4
    
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
                return "Kapacitet"
            elif section == 2 and role == QtCore.Qt.DisplayRole:
                return "Broj zauzetih mesta"
            elif section == 3 and role == QtCore.Qt.DisplayRole:
                return "Radna temperatura hale"

    def get_element(self, index: QtCore.QModelIndex):
        if index.isValid():
            element = self._podaci[index.row()][index.column()]
            if element:
                return element
        return None

    def ucitaj_podatke(self):
        dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_podaci.txt",'r')
        while True:
            s = []
            naziv = dat.read(10).strip()
            if naziv=="":
                break
            kapacitet = dat.read(5).strip()
            broj_zauzetih_mesta = dat.read(5).strip()
            temperatura = dat.read(3).strip()
            dat.read(1)
            s.append(naziv)
            s.append(int(kapacitet))
            s.append(broj_zauzetih_mesta)
            if temperatura == "1":
                s.append("od -10C do 0C")
            elif temperatura == "2":
                s.append("od 1C do 18C")
            else:
                s.append("od 19C do 25C")
            self._podaci.append(s)
        dat.close()