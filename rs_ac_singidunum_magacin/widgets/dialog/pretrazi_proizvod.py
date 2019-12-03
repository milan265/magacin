from PySide2 import QtWidgets, QtGui, QtCore
from ...proizvod import Proizvod
from ...proizvod_podaci import ProizvodPodaci

class PretraziProizvod(QtWidgets.QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Pretraži proizvod")
        self.setWindowIcon(QtGui.QIcon("resources/icons/magnifier.png"))
        self.resize(350,400)
    
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.hbox_layout = QtWidgets.QHBoxLayout()
        self.line_edit_naziv = QtWidgets.QLineEdit(self)
        self.list_widget_proizvodi = QtWidgets.QListWidget()
        self.dialog_button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, parent=self)
        
        self.hbox_layout.addWidget(self.line_edit_naziv)

        self.list_widget_proizvodi.setStyleSheet("QListWidget { font-family: Courier }")
        self.line_edit_naziv.setPlaceholderText("Naziv proizvoda")

        self.vbox_layout.addLayout(self.hbox_layout)
        self.vbox_layout.addWidget(self.list_widget_proizvodi)
        self.vbox_layout.addWidget(self.dialog_button_box)

        self.dialog_button_box.accepted.connect(self._ok)
        self.dialog_button_box.rejected.connect(self.reject)

        self.setLayout(self.vbox_layout)

        self.proizvod_podaci_lista = ProizvodPodaci().proizvod_lista
        
        self._popuni_list_widget_proizvodi()
        self.line_edit_naziv.textChanged.connect(self._popuni_list_widget_proizvodi)
        self._vrednost = ""

    def _ok(self):
        t = False
        for i in range(self.list_widget_proizvodi.count()):
            if self.list_widget_proizvodi.item(i).isSelected():
                t = True
                break
        if t:
            self._vrednost = self.list_widget_proizvodi.item(i).text()
            self.accept()
        else:
            return
    
    def _popuni_list_widget_proizvodi(self):
        self.list_widget_proizvodi.clear()
        tekst = self.line_edit_naziv.text()
        regex = QtCore.QRegExp("*"+tekst+"*", QtCore.Qt.CaseInsensitive)
        regex.setPatternSyntax(QtCore.QRegExp.Wildcard) 
        for i in self.proizvod_podaci_lista:
            if  regex.exactMatch(i.naziv):
                self.list_widget_proizvodi.addItem("{0:15s}{1:13s}{2:8d}".format(i.naziv,i.rok_upotrebe,i.kolicina))
        
    def nadjen_proizvod(self):
        return self._vrednost