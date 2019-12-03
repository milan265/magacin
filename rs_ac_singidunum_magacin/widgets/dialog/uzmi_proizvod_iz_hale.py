from PySide2 import QtWidgets, QtGui
from ...proizvod import Proizvod

class UzmiProizvodIzHale(QtWidgets.QDialog):

    def __init__(self, max_kolicina, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Uzmi proizvod iz hale")
        self.setWindowIcon(QtGui.QIcon("resources/icons/fruit.png"))

        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        self.spin_box_kolicina = QtWidgets.QSpinBox()
        self.dialog_button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, parent=self)

        self.spin_box_kolicina.setMinimum(1)
        self.spin_box_kolicina.setMaximum(max_kolicina)

        self.dialog_button_box.accepted.connect(self.accept)
        self.dialog_button_box.rejected.connect(self.reject)

        self.form_layout.addRow("Količina:", self.spin_box_kolicina)
       
        self.vbox_layout.addLayout(self.form_layout)
        self.vbox_layout.addWidget(self.dialog_button_box)

        self.setLayout(self.vbox_layout)

    def podaci(self):
        return int(self.spin_box_kolicina.text())