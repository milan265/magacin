from PySide2 import QtWidgets, QtCore, QtGui
from ...proizvod import Proizvod
from ...proizvod_podaci import ProizvodPodaci

class DodajProizvod(QtWidgets.QDialog):

    def __init__(self, parent=None, dodaj=True, proizvod=None):

        super().__init__(parent)

        if dodaj:
            self.setWindowTitle("Dodaj proizvod")
            self.setWindowIcon(QtGui.QIcon("resources/icons/fruit.png"))
        else:
            self.setWindowTitle("Izmeni proizvod")
            self.setWindowIcon(QtGui.QIcon("resources/icons/fruit-apple-half.png"))
        self._dodaj = dodaj
        self._proizvod = proizvod

        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        self.line_edit_naziv = QtWidgets.QLineEdit(self)
        self.date_edit_rok_upotrebe = QtWidgets.QDateEdit(self)
        self.spin_box_temperatura = QtWidgets.QSpinBox()
        self.spin_box_kolicina = QtWidgets.QSpinBox()
        self.dialog_button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, parent=self)

        self.line_edit_naziv.setMaxLength(14)
        self.spin_box_kolicina.setMinimum(1)
        self.spin_box_kolicina.setMaximum(250)
        self.spin_box_temperatura.setMinimum(-10)
        self.spin_box_temperatura.setMaximum(25)
        self.date_edit_rok_upotrebe.setDate(QtCore.QDate.currentDate())
        self.date_edit_rok_upotrebe.setMinimumDate(QtCore.QDate.currentDate())
        self.date_edit_rok_upotrebe.setCalendarPopup(True)
        self.date_edit_rok_upotrebe.setDisplayFormat("dd.MM.yyyy")
        self.date_edit_rok_upotrebe.setMinimumDate(QtCore.QDate.currentDate())

        if not dodaj:
            self.line_edit_naziv.setText(proizvod.naziv)
            self.date_edit_rok_upotrebe.setDate(QtCore.QDate(int(proizvod.rok_upotrebe[6:]), int(proizvod.rok_upotrebe[3:5]), int(proizvod.rok_upotrebe[:2])))
            self.spin_box_temperatura.setValue(proizvod.temperatura)
            self.spin_box_kolicina.setValue(proizvod.kolicina)
        
        self.form_layout.addRow("Naziv:", self.line_edit_naziv)
        self.form_layout.addRow("Rok upotrebe:", self.date_edit_rok_upotrebe)
        self.form_layout.addRow("Temperatura:", self.spin_box_temperatura)
        self.form_layout.addRow("Količina:", self.spin_box_kolicina)

        self.vbox_layout.addLayout(self.form_layout)
        self.vbox_layout.addWidget(self.dialog_button_box)

        self.dialog_button_box.accepted.connect(self._ok)
        self.dialog_button_box.rejected.connect(self.reject)

        self.setLayout(self.vbox_layout)


    def _ok(self):
        if self.line_edit_naziv.text() == "":
            QtWidgets.QMessageBox.warning(self, "Provera naziva proizvoda", "Polje naziv mora biti popunjeno!", QtWidgets.QMessageBox.Ok)
            return
        if not self._dodaj:
            proizvod_podaci = ProizvodPodaci()
            pr = proizvod_podaci.nadji_proizvod(self.line_edit_naziv.text(), self.date_edit_rok_upotrebe.text())
            if pr != None and (pr.naziv !=  self._proizvod.naziv and pr.rok_upotrebe !=  self._proizvod.rok_upotrebe):
                QtWidgets.QMessageBox.warning(self, "Provera", "Proizvod već postoji! \n Nije moguće izmeniti proizvod!", QtWidgets.QMessageBox.Ok)
                return  
        self.accept()
        
    def podaci_o_proizvodu(self):
        proizvod = Proizvod(self.line_edit_naziv.text(), self.date_edit_rok_upotrebe.text(), self.spin_box_temperatura.value(), self.spin_box_kolicina.value())
        return proizvod