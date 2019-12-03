from PySide2 import QtWidgets, QtCore, QtGui
from ...proizvod_podaci import ProizvodPodaci
from ...magacin_podaci import MagacinPodaci
from ...magacin_proizvod import MagacinProizvod

class DodajProizvodUHalu(QtWidgets.QDialog):

    def __init__(self, hala, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Dodaj proizvod u halu")
        self.setWindowIcon(QtGui.QIcon("resources/icons/fruit.png"))

        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        self.combo_box_proizvod = QtWidgets.QComboBox()
        self.spin_box_kolicina = QtWidgets.QSpinBox()
        self.date_edit = QtWidgets.QDateEdit(self)
        self.dialog_button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, parent=self)

        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        self.date_edit.setMinimumDate(QtCore.QDate.currentDate())
        self.spin_box_kolicina.setMinimum(1)
        self.combo_box_proizvod.setStyleSheet("QComboBox { font-family: Courier }")

        self.date_edit.setEnabled(False)
        self.spin_box_kolicina.setEnabled(False)

        self.dialog_button_box.accepted.connect(self._ok)
        self.dialog_button_box.rejected.connect(self.reject)

        self.form_layout.addRow("Proizvod:", self.combo_box_proizvod)
        self.form_layout.addRow("Količina:", self.spin_box_kolicina)
        self.form_layout.addRow("Datum isteka:", self.date_edit)

        self.vbox_layout.addLayout(self.form_layout)
        self.vbox_layout.addWidget(self.dialog_button_box)

        self.setLayout(self.vbox_layout)

        self._lista_combo = []
        self._popuni_combo_box(hala)

        self.combo_box_proizvod.currentIndexChanged.connect(self._podesi_formu)


    def _ok(self):
        if self.combo_box_proizvod.currentIndex() == 0:
            return
        self.accept()

    def _popuni_combo_box(self,hala):
        magacin_podaci = MagacinPodaci()
        temp = magacin_podaci.nadji_halu(hala).temperatura
        self.combo_box_proizvod.addItem("Proizvodi")
        self.combo_box_proizvod.model().item(0).setFlags(QtCore.Qt.ItemIsEnabled)
        proizvod_podaci = ProizvodPodaci()
        for i in proizvod_podaci.proizvod_lista:
            if temp == 1 and i.temperatura >= -10 and i.temperatura <= 0:
                self.combo_box_proizvod.addItem("{0:15s}{1:10s}".format(i.naziv,i.rok_upotrebe))
                self._lista_combo.append(i)
            elif temp == 2 and i.temperatura >= 1 and i.temperatura <=18:
                self.combo_box_proizvod.addItem("{0:15s}{1:10s}".format(i.naziv,i.rok_upotrebe))
                self._lista_combo.append(i)
            elif temp == 3 and i.temperatura >= 19 and i.temperatura <=25:
                self.combo_box_proizvod.addItem("{0:15s}{1:10s}".format(i.naziv,i.rok_upotrebe))
                self._lista_combo.append(i)
    
    def _podesi_formu(self):
        self.date_edit.setEnabled(True)
        self.spin_box_kolicina.setEnabled(True)
        naziv_proizvoda = self.combo_box_proizvod.currentText()[:15].strip()
        rok_upotrebe = self.combo_box_proizvod.currentText()[15:].strip()
        proizvod_podaci = ProizvodPodaci()
        proizvod = proizvod_podaci.nadji_proizvod(naziv_proizvoda, rok_upotrebe)
        self.date_edit.setMaximumDate(QtCore.QDate(int(proizvod.rok_upotrebe[6:]), int(proizvod.rok_upotrebe[3:5]), int(proizvod.rok_upotrebe[:2])))
        self.spin_box_kolicina.setMaximum(proizvod.kolicina)

    def podaci_za_tabelu(self, hala):
        magacin_podaci = MagacinPodaci()
        h = magacin_podaci.nadji_halu(hala)
        naziv_proizvoda = self.combo_box_proizvod.currentText()[:15].strip()
        rok_upotrebe = self.combo_box_proizvod.currentText()[15:].strip()
        proizvod_podaci = ProizvodPodaci()
        p = proizvod_podaci.nadji_proizvod(naziv_proizvoda, rok_upotrebe)
        return MagacinProizvod(h.naziv,p.naziv,p.rok_upotrebe,QtCore.QDate.currentDate().toString("dd.MM.yyyy"),self.date_edit.text(),p.temperatura,h.temperatura,self.spin_box_kolicina.value())