from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from .dialog.dodaj_halu import DodajHalu
from .dialog.dodaj_proizvod import DodajProizvod
from .dialog.dodaj_proizvod_u_halu import DodajProizvodUHalu
from .dialog.uzmi_proizvod_iz_hale import UzmiProizvodIzHale
from .dialog.pretrazi_proizvod import PretraziProizvod
from ..magacin_podaci import MagacinPodaci
from ..proizvod_podaci import ProizvodPodaci
from ..magacin_proizvod_podaci import MagacinProizvodPodaci
from ..hala import Hala
from ..proizvod import Proizvod
from ..magacin_proizvod import MagacinProizvod
from ..tabela_model import TabelaModel
from ..tabela_istorija import TabelaIstorija
from ..tabela_sve_hale import TabelaSveHale

class Magacin(QtWidgets.QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.hbox_layout_hala = QtWidgets.QHBoxLayout()
        self.vbox_layout_prikaz = QtWidgets.QVBoxLayout()
        self.hbox_layout_proizvod = QtWidgets.QHBoxLayout()
        self.hbox_layout_proizvod_hala = QtWidgets.QHBoxLayout()
        self.combo_box_hala = QtWidgets.QComboBox()
        self.combo_box_proizvod = QtWidgets.QComboBox()
        self.push_button_dodaj_halu = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/plus.png"), "Dodaj halu", self)
        self.push_button_obrisi_halu = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/minus.png"), "Obriši halu", self)
        self.push_button_prikazi_halu = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/store-medium.png"), "Prikaži halu", self)
        self.push_button_prikazi_sve_hale = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/store.png"), "Prikaži sve hale", self)
        self.push_button_prikazi_istoriju_dodavanja = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/clock-history.png"), "Prikaži istoriju dodavanja", self)
        self.push_button_pretrazi_proizvod = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/magnifier.png"), "Pretraži proizvod", self)
        self.push_button_dodaj_proizvod = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/plus.png"), "Dodaj proizvod", self)
        self.push_button_izmeni_proizvod = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/arrow-circle-double-135.png"), "Izmeni proizvod", self)
        self.push_button_obrisi_proizvod = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/minus.png"), "Obriši proizvod", self)
        self.label_podaci = QtWidgets.QLabel(self)
        self.table_view_proizvodi = QtWidgets.QTableView(self)
        self.push_button_dodaj_proizvod_u_halu = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/plus.png"), "Dodaj proizvod u halu", self)
        self.push_button_uzmi_proizvod_iz_hale = QtWidgets.QPushButton(QtGui.QIcon("resources/icons/minus.png"), "Uzmi proizvod iz hale", self)

        self.hbox_layout_hala.addWidget(self.combo_box_hala)
        self.hbox_layout_hala.addWidget(self.push_button_dodaj_halu)
        self.hbox_layout_hala.addWidget(self.push_button_obrisi_halu)
        self.hbox_layout_hala.addWidget(self.push_button_prikazi_halu)
        self.hbox_layout_hala.addWidget(self.push_button_prikazi_sve_hale)
        self.hbox_layout_hala.addWidget(self.push_button_prikazi_istoriju_dodavanja)

        self.push_button_dodaj_halu.clicked.connect(self._dodaj_halu)
        self.push_button_obrisi_halu.clicked.connect(self._obrisi_halu)
        self.push_button_prikazi_halu.clicked.connect(self._prikazi_halu)
        self.push_button_prikazi_sve_hale.clicked.connect(self._prikazi_sve_hale)
        self.push_button_prikazi_istoriju_dodavanja.clicked.connect(self._prikazi_istoriju_dodavanja)

        self.hbox_layout_proizvod.addWidget(self.combo_box_proizvod)
        self.hbox_layout_proizvod.addWidget(self.push_button_pretrazi_proizvod)
        self.hbox_layout_proizvod.addWidget(self.push_button_dodaj_proizvod)
        self.hbox_layout_proizvod.addWidget(self.push_button_izmeni_proizvod)
        self.hbox_layout_proizvod.addWidget(self.push_button_obrisi_proizvod)

        self.push_button_pretrazi_proizvod.clicked.connect(self._pretrazi_proizvod)
        self.push_button_dodaj_proizvod.clicked.connect(self._dodaj_proizvod)
        self.push_button_izmeni_proizvod.clicked.connect(self._izmeni_proizvod)
        self.push_button_obrisi_proizvod.clicked.connect(self._obrisi_proizvod)

        self.hbox_layout_proizvod_hala.addWidget(self.push_button_dodaj_proizvod_u_halu)
        self.hbox_layout_proizvod_hala.addWidget(self.push_button_uzmi_proizvod_iz_hale)

        self.push_button_dodaj_proizvod_u_halu.clicked.connect(self._dodaj_proizvod_u_halu)
        self.push_button_uzmi_proizvod_iz_hale.clicked.connect(self._uzmi_proizvod_iz_hale)
        
        self.vbox_layout_prikaz.addWidget(self.label_podaci)
        self.vbox_layout_prikaz.addWidget(self.table_view_proizvodi)
        self.vbox_layout_prikaz.addLayout(self.hbox_layout_proizvod_hala)

        self.vbox_layout.addLayout(self.hbox_layout_hala)
        self.vbox_layout.addLayout(self.hbox_layout_proizvod)
        self.vbox_layout.addLayout(self.vbox_layout_prikaz)

        self.setLayout(self.vbox_layout)

        self.label_podaci.setVisible(False)
        self.push_button_dodaj_proizvod_u_halu.setVisible(False)
        self.push_button_uzmi_proizvod_iz_hale.setVisible(False)

        #za sortiranje po kolonama
        self.proxyModel = QtCore.QSortFilterProxyModel()

        self.aktivna_hala = ""
        self.istorija = False
        self.sve_hale = False

        self.table_view_proizvodi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_view_proizvodi.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        
        self.temperature = {
            1 : 'od -10C do 0C',
            2 : 'od 1C do 18C',
            3 : 'od 19C do 25C'
        }

        #podesen font zbog formatiranog prikaza
        self.combo_box_hala.setStyleSheet("QComboBox { font-family: Courier }")
        self.combo_box_proizvod.setStyleSheet("QComboBox { font-family: Courier }")

        self._popuni_combo_box_hala()
        self._popuni_combo_box_proizvod()

    def _isprazni_combo_box(self, combo_box):
        for i in range(combo_box.count()):
            combo_box.removeItem(0)

    def _popuni_combo_box_hala(self):
        hale = MagacinPodaci()
        self.combo_box_hala.addItem("Hale")
        self.combo_box_hala.model().item(0).setFlags(QtCore.Qt.ItemIsEnabled)
        k=0
        for i in range(1,4):    
            self.combo_box_hala.addItem(self.temperature[i])
            k = k+1
            self.combo_box_hala.model().item(k).setFlags(QtCore.Qt.ItemIsEnabled)
            for element in hale.magacin_lista:
                if element.temperatura == i:
                    self.combo_box_hala.addItem(element.naziv)
                    k = k+1


    def _dodaj_halu(self):
        dialog = DodajHalu(self.parent())
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            nova_hala = dialog.podaci_o_novoj_hali()
            dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_podaci.txt",'a')
            dat.write("{0:10s}{1:5d}{2:5d}{3:3d}".format(nova_hala.naziv, nova_hala.kapacitet, nova_hala.broj_zauzetih_mesta, nova_hala.temperatura))
            dat.write("\n")
            dat.flush()
            dat.close()
            self._isprazni_combo_box(self.combo_box_hala)
            self._popuni_combo_box_hala()

    def _obrisi_halu(self):
        tekst = self.combo_box_hala.currentText()
        if self.combo_box_hala.currentIndex()!=0 and tekst!=self.temperature[1] and tekst!=self.temperature[2] and tekst!=self.temperature[3] and tekst!=self.aktivna_hala:
            magacin_podaci = MagacinPodaci()
            hala = magacin_podaci.nadji_halu(tekst)
            if hala.broj_zauzetih_mesta == 0:
                odgovor = QtWidgets.QMessageBox.question(self, "Brisanje hale", "Da li želite da obrišete halu sa nazivom "+tekst+"?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
                if odgovor == QtWidgets.QMessageBox.Yes:
                    self.combo_box_hala.removeItem(self.combo_box_hala.currentIndex())
                    magacin_lista = magacin_podaci.magacin_lista
                    for i in magacin_lista:
                        if i.naziv == tekst:
                            magacin_lista.remove(i)
                            break
                    dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_podaci.txt",'w')
                    for i in magacin_lista:
                        dat.write("{0:10s}{1:5d}{2:5d}{3:3d}".format(i.naziv, i.kapacitet, i.broj_zauzetih_mesta, i.temperatura))
                        dat.write("\n")
                    dat.flush()
                    dat.close()
                    self.combo_box_hala.setCurrentIndex(0)
            else:
                QtWidgets.QMessageBox.warning(self, "Brisanje hale", "Ne može se brisati hala u kojoj se nalazi neki proizvod!", QtWidgets.QMessageBox.Ok)

    def set_model(self, model=None):
        self.table_view_proizvodi.setModel(model)

    def _prikazi_halu(self):
        self.table_view_proizvodi.setSortingEnabled(True)
        #postavljamo strelicu za sortiranje na 99. kolonu zato sto ta kolona ne postoji
        self.table_view_proizvodi.sortByColumn(99,QtCore.Qt.AscendingOrder)
        self.table_view_proizvodi.reset()
        self.table_view_proizvodi.show()
        self.istorija = False
        self.sve_hale = False
        tekst = self.combo_box_hala.currentText()
        if self.combo_box_hala.currentIndex()!=0 and tekst!=self.temperature[1] and tekst!=self.temperature[2] and tekst!=self.temperature[3] and tekst!=self.aktivna_hala:
            magacin_podaci = MagacinPodaci()
            hala = magacin_podaci.nadji_halu(tekst)
            self.label_podaci.setText(hala.naziv+" "*10+" radna temperatura: "+self.temperature[hala.temperatura]+" "*10+" iskorišćenost: "+str(hala.broj_zauzetih_mesta)+"/"+str(hala.kapacitet))
            self.label_podaci.setStyleSheet("QLabel { margin: 2px ; font: 14px }")
            self.label_podaci.setVisible(True)
            self.push_button_dodaj_proizvod_u_halu.setVisible(True)
            self.push_button_uzmi_proizvod_iz_hale.setVisible(True)
            self.aktivna_hala = hala.naziv
            self.proxyModel.setSourceModel(TabelaModel(tekst))
            self.set_model(self.proxyModel)
        elif tekst==self.aktivna_hala:
            self.label_podaci.setVisible(False)
            self.push_button_dodaj_proizvod_u_halu.setVisible(False)
            self.push_button_uzmi_proizvod_iz_hale.setVisible(False)
            self.aktivna_hala = ""
            self.set_model()

    def _prikazi_istoriju_dodavanja(self):
        self.table_view_proizvodi.setSortingEnabled(False)
        self.label_podaci.setVisible(False)
        self.push_button_dodaj_proizvod_u_halu.setVisible(False)
        self.push_button_uzmi_proizvod_iz_hale.setVisible(False)
        self.aktivna_hala = ""
        self.sve_hale = False
        if not self.istorija:
            self.set_model(TabelaIstorija())
            self.istorija = True
        else:
            self.set_model()
            self.istorija = False
    
    def _prikazi_sve_hale(self):
        self.table_view_proizvodi.setSortingEnabled(True)
        self.table_view_proizvodi.sortByColumn(99,QtCore.Qt.AscendingOrder)
        self.table_view_proizvodi.reset()
        self.table_view_proizvodi.show()
        self.label_podaci.setVisible(False)
        self.push_button_dodaj_proizvod_u_halu.setVisible(False)
        self.push_button_uzmi_proizvod_iz_hale.setVisible(False)
        self.aktivna_hala = ""
        self.istorija = False
        if not self.sve_hale:
            self.proxyModel.setSourceModel(TabelaSveHale())
            self.set_model(self.proxyModel)
            self.sve_hale = True
        else:
            self.set_model()
            self.sve_hale = False

    def _popuni_combo_box_proizvod(self):
        proizvodi = ProizvodPodaci()
        self.combo_box_proizvod.addItem("Proizvodi")
        self.combo_box_proizvod.model().item(0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.combo_box_proizvod.addItem("{0:15s}{1:13s}{2:>8s}".format("Naziv","Rok upotrebe","Količina"))
        self.combo_box_proizvod.model().item(1).setFlags(QtCore.Qt.ItemIsEnabled)
        for i in proizvodi.proizvod_lista:
            self.combo_box_proizvod.addItem("{0:15s}{1:13s}{2:8d}".format(i.naziv,i.rok_upotrebe,i.kolicina))

    def _pretrazi_proizvod(self):
        dialog = PretraziProizvod(self.parent())
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            proizvod = dialog.nadjen_proizvod()
            for i in range(2,self.combo_box_proizvod.count(),1):
                if proizvod == self.combo_box_proizvod.itemText(i):
                    self.combo_box_proizvod.setCurrentIndex(i)
                    break


    def _dodaj_proizvod(self):
        dialog = DodajProizvod(self.parent())
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            nov_proizvod = dialog.podaci_o_proizvodu()
            proizvod_podaci = ProizvodPodaci()
            nalazi_se = False
            pozicija = 0
            for i in proizvod_podaci.proizvod_lista:
                if i.naziv == nov_proizvod.naziv and i.rok_upotrebe == nov_proizvod.rok_upotrebe:
                    trenutna_kolicina = i.kolicina
                    nalazi_se = True
                    break
                pozicija += 1
            if not nalazi_se:
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/proizvod_podaci.txt",'a')
                dat.write("{0:15s}{1:>13s}{2:3d}{3:5d}".format(nov_proizvod.naziv, nov_proizvod.rok_upotrebe, nov_proizvod.temperatura, nov_proizvod.kolicina))
                dat.write("\n")
                dat.flush()
                dat.close()
            else:
                nov_proizvod.kolicina += trenutna_kolicina
                proizvod_podaci.proizvod_lista.insert(pozicija,nov_proizvod)
                del proizvod_podaci.proizvod_lista[pozicija+1]
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/proizvod_podaci.txt",'w')
                for i in proizvod_podaci.proizvod_lista:
                    dat.write("{0:15s}{1:>13s}{2:3d}{3:5d}".format(i.naziv, i.rok_upotrebe, i.temperatura, i.kolicina))
                    dat.write("\n")
                dat.flush()
                dat.close()
            self._isprazni_combo_box(self.combo_box_proizvod)
            self._popuni_combo_box_proizvod()

    def _izmeni_proizvod(self):
        indeks = self.combo_box_proizvod.currentIndex()
        tekst = self.combo_box_proizvod.currentText()
        if indeks != 0 and indeks != 1:
            naziv = tekst[:15].strip()
            rok_upotrebe = tekst[15:28].strip()
            proizvod_podaci = ProizvodPodaci()
            proizvod = proizvod_podaci.nadji_proizvod(naziv, rok_upotrebe)
            dialog = DodajProizvod(self.parent(), False, proizvod)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                nov_proizvod = dialog.podaci_o_proizvodu()
                proizvod_podaci.proizvod_lista.insert(indeks-2,nov_proizvod)
                del proizvod_podaci.proizvod_lista[indeks-1]
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/proizvod_podaci.txt",'w')
                for i in proizvod_podaci.proizvod_lista:
                    dat.write("{0:15s}{1:>13s}{2:3d}{3:5d}".format(i.naziv, i.rok_upotrebe, i.temperatura, i.kolicina))
                    dat.write("\n")
                dat.flush()
                dat.close()
                self._isprazni_combo_box(self.combo_box_proizvod)
                self._popuni_combo_box_proizvod()
                
    
    def _obrisi_proizvod(self):
        indeks = self.combo_box_proizvod.currentIndex()
        tekst = self.combo_box_proizvod.currentText()
        if indeks != 0 and indeks != 1:
            odgovor = QtWidgets.QMessageBox.question(self, "Brisanje proizvoda", "Da li želite da obrišete proizvod "+tekst[:15].strip()+" "+tekst[15:28].strip()+"?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            if odgovor == QtWidgets.QMessageBox.Yes:
                self.combo_box_proizvod.removeItem(indeks)
                proizvod_podaci = ProizvodPodaci()
                proizvod_lista = proizvod_podaci.proizvod_lista
                del proizvod_lista[indeks-2]
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/proizvod_podaci.txt",'w')
                for i in proizvod_lista:
                    dat.write("{0:15s}{1:>13s}{2:3d}{3:5d}".format(i.naziv, i.rok_upotrebe, i.temperatura, i.kolicina))
                    dat.write("\n")
                dat.flush()
                dat.close()
        if self.combo_box_proizvod.count()==2:
            self.combo_box_proizvod.setCurrentIndex(0)

    def lista_magacin_proizvod(self):
        magacin_proizvod_podaci = MagacinProizvodPodaci()
        lista = magacin_proizvod_podaci._magacin_proizvod_lista
        for i in range(len(lista)-1):
            for j in range(i+1, len(lista), 1):
                if lista[i].naziv_hale == lista[j].naziv_hale and lista[i].naziv_proizvoda == lista[j].naziv_proizvoda and lista[i].rok_upotrebe == lista[j].rok_upotrebe and lista[i].kolicina != 0 and lista[j].kolicina != 0:
                    lista[i].kolicina += lista[j].kolicina
                    lista[j].kolicina = 0
        for i in range(len(lista)-1, -1, -1):
            if lista[i].kolicina == 0:
                del lista[i]
        return lista

    def _dodaj_proizvod_u_halu(self):
        hala = self.combo_box_hala.currentText()
        dialog = DodajProizvodUHalu(hala, self.parent())
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            p = dialog.podaci_za_tabelu(hala)
            upisuj = True
            magacin_podaci = MagacinPodaci()
            proizvod_podaci = ProizvodPodaci()
            for i in magacin_podaci.magacin_lista:
                if p.naziv_hale == i.naziv:
                    br_slobodnih_mesta = i.kapacitet - i.broj_zauzetih_mesta
                    if br_slobodnih_mesta >= p.kolicina:
                        i.broj_zauzetih_mesta += p.kolicina
                        break
                    else:
                        QtWidgets.QMessageBox.warning(self, "Provera", "Nema više slobodnih mesta u hali!", QtWidgets.QMessageBox.Ok)
                        upisuj = False
                        break
            if upisuj:
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/istorija.txt","a")
                dat.write("{0:10s}{1:15s}{2:11s}{3:11s}{4:11s}{5:4d}{6:2d}{7:4d}".format(p.naziv_hale,p.naziv_proizvoda,p.rok_upotrebe,p.datum_dodavanja,p.datum_isteka,p.temperatura_proizvoda,p.temperatura_hale,p.kolicina))
                dat.write("\n")
                dat.flush()
                dat.close()
            
                lista = self.lista_magacin_proizvod()
                dat =open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_proizvod.txt","w")
                for i in lista:
                    dat.write("{0:10s}{1:15s}{2:11s}{3:11s}{4:11s}{5:4s}{6:2s}{7:4d}".format(i.naziv_hale, i.naziv_proizvoda, i.rok_upotrebe, i.datum_dodavanja, i.datum_isteka, i.temperatura_proizvoda,i.temperatura_hale, i.kolicina))
                    dat.write("\n")
                dat.flush()
                dat.close()

                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_podaci.txt",'w')
                for i in magacin_podaci.magacin_lista:
                    dat.write("{0:10s}{1:5d}{2:5d}{3:3d}".format(i.naziv, i.kapacitet, i.broj_zauzetih_mesta, i.temperatura))
                    dat.write("\n")
                dat.flush()
                dat.close()
                    
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/proizvod_podaci.txt",'w')
                for i in range(len(proizvod_podaci.proizvod_lista)):
                    if p.naziv_proizvoda == proizvod_podaci.proizvod_lista[i].naziv and p.rok_upotrebe == proizvod_podaci.proizvod_lista[i].rok_upotrebe:
                        proizvod_podaci.proizvod_lista[i].kolicina -= p.kolicina
                        if proizvod_podaci.proizvod_lista[i].kolicina == 0:
                            del proizvod_podaci.proizvod_lista[i]
                            break
                for i in proizvod_podaci.proizvod_lista:
                    dat.write("{0:15s}{1:>13s}{2:3d}{3:5d}".format(i.naziv, i.rok_upotrebe, i.temperatura, i.kolicina))
                    dat.write("\n")
                dat.flush()
                dat.close()
                self._isprazni_combo_box(self.combo_box_proizvod)
                self._popuni_combo_box_proizvod()

                #Ovo radimo da bi se osvezila tabela sa novim podacima, prikazuje tabelu sa novim podacima
                self.aktivna_hala = ""
                self._prikazi_halu()

    def _uzmi_proizvod_iz_hale(self):
        #proveravamo da li je selektovan proizvod u tabeli, selectedIndexes() je lista
        if self.table_view_proizvodi.selectedIndexes() == []:
            QtWidgets.QMessageBox.warning(self, "Upozorenje", "Morate selektovati proizvod u tabeli", QtWidgets.QMessageBox.Ok)
        else:
            kolicna = int(self.table_view_proizvodi.model().sourceModel().get_element(self.table_view_proizvodi.selectedIndexes()[5]))
            dialog = UzmiProizvodIzHale(kolicna,self.parent())
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                #kolicna -= dialog.podaci()
                #if kolicna != 0:
                    #self.table_view_proizvodi.model().promeni_vrednost_kolicne(self.table_view_proizvodi.selectedIndexes()[0].row(),kolicna)
                #else:
                    #self.table_view_proizvodi.model().ukloni_proizvod(self.table_view_proizvodi.selectedIndexes()[0].row())
               
                #promena_kolicine je negativan broj unesene kolicine u dialogu
                promena_kolicne = dialog.podaci()-2*dialog.podaci()
                naziv_hale = self.combo_box_hala.currentText()
                naziv_proizvoda = self.table_view_proizvodi.model().sourceModel().get_element(self.table_view_proizvodi.selectedIndexes()[0])
                rok_upotrebe = self.table_view_proizvodi.model().sourceModel().get_element(self.table_view_proizvodi.selectedIndexes()[1])
                magacin_proizvod_podaci = MagacinProizvodPodaci()
                p = magacin_proizvod_podaci.nadji_magacin_proizvod(naziv_hale, naziv_proizvoda, rok_upotrebe)
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/istorija.txt","a")
                dat.write("{0:10s}{1:15s}{2:11s}{3:11s}{4:11s}{5:4d}{6:2d}{7:4d}".format(p.naziv_hale,p.naziv_proizvoda,p.rok_upotrebe,QtCore.QDate.currentDate().toString("dd.MM.yyyy"),p.datum_isteka,int(p.temperatura_proizvoda),int(p.temperatura_hale),promena_kolicne))
                dat.write("\n")
                dat.flush()
                dat.close()

                lista = self.lista_magacin_proizvod()
                dat =open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_proizvod.txt","w")
                for i in lista:
                    dat.write("{0:10s}{1:15s}{2:11s}{3:11s}{4:11s}{5:4s}{6:2s}{7:4d}".format(i.naziv_hale, i.naziv_proizvoda, i.rok_upotrebe, i.datum_dodavanja, i.datum_isteka, i.temperatura_proizvoda,i.temperatura_hale, i.kolicina))
                    dat.write("\n")
                dat.flush()
                dat.close()

                magacin_podaci = MagacinPodaci()
                dat = open("./plugins/rs_ac_singidunum_magacin/podaci/magacin_podaci.txt",'w')
                for i in magacin_podaci.magacin_lista:
                    if i.naziv == naziv_hale:
                        broj_zauzetih_mesta = i.broj_zauzetih_mesta - dialog.podaci()
                    else:
                        broj_zauzetih_mesta = i.broj_zauzetih_mesta
                    dat.write("{0:10s}{1:5d}{2:5d}{3:3d}".format(i.naziv, i.kapacitet, broj_zauzetih_mesta, i.temperatura))
                    dat.write("\n")
                dat.flush()
                dat.close()

                self.aktivna_hala = ""
                self._prikazi_halu()