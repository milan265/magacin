from PySide2 import QtWidgets, QtGui
from ...hala import Hala
from ...magacin_podaci import MagacinPodaci

class DodajHalu(QtWidgets.QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Dodaj halu")
        self.setWindowIcon(QtGui.QIcon("resources/icons/block.png"))
    
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.hbox_layout = QtWidgets.QHBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        self.line_edit_naziv = QtWidgets.QLineEdit(self)
        self.spin_box_kapacitet = QtWidgets.QSpinBox()
        self.radio_button_temperatura_0 = QtWidgets.QRadioButton("-10C - 0C", self)
        self.radio_button_temperatura_18 = QtWidgets.QRadioButton("1C - 18C", self)
        self.radio_button_temperatura_25 = QtWidgets.QRadioButton("19C - 25C", self)
        self.dialog_button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, parent=self)
        
        self.line_edit_naziv.setMaxLength(10)
        self.spin_box_kapacitet.setMinimum(1)
        self.spin_box_kapacitet.setMaximum(1000)

        self.hbox_layout.addWidget(self.radio_button_temperatura_0)
        self.hbox_layout.addWidget(self.radio_button_temperatura_18)
        self.hbox_layout.addWidget(self.radio_button_temperatura_25)

        self.form_layout.addRow("Naziv:", self.line_edit_naziv)
        self.form_layout.addRow("Kapacitet:",self.spin_box_kapacitet)
        self.form_layout.addRow(self.hbox_layout)

        self.vbox_layout.addLayout(self.form_layout)
        self.vbox_layout.addWidget(self.dialog_button_box)

        self.dialog_button_box.accepted.connect(self._ok)
        self.dialog_button_box.rejected.connect(self.reject)

        self.setLayout(self.vbox_layout)

    def _ok(self):
        magacin_podaci = MagacinPodaci()
        if self.line_edit_naziv.text() == "":
            QtWidgets.QMessageBox.warning(self, "Provera naziva hale", "Polje naziv mora biti popunjeno!", QtWidgets.QMessageBox.Ok)
            return
        for element in magacin_podaci.magacin_lista:
            if element.naziv == self.line_edit_naziv.text():
                QtWidgets.QMessageBox.warning(self, "Provera naziva hale", "Hala sa tim nazivom vec postoji!", QtWidgets.QMessageBox.Ok)
                return
        if not(self.radio_button_temperatura_0.isChecked() or self.radio_button_temperatura_18.isChecked() or self.radio_button_temperatura_25.isChecked()):
            QtWidgets.QMessageBox.warning(self, "Provera radne temperature", "Morate odabrati radnu temperaturu hale!", QtWidgets.QMessageBox.Ok)
            return
        self.accept()
    
    def podaci_o_novoj_hali(self):
        temp = 0
        if self.radio_button_temperatura_0.isChecked():
            temp = 1
        elif self.radio_button_temperatura_18.isChecked():
            temp = 2
        elif self.radio_button_temperatura_25.isChecked():
            temp = 3
        hala = Hala(self.line_edit_naziv.text(), self.spin_box_kapacitet.value(), 0, temp)
        return hala