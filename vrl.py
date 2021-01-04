from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QAbstractTableModel, Qt
from tinydb import TinyDB, Query
from PyQt5.QtCore import Qt
import os
import pandas as pd
import math


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        try:
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:

                return self._data.columns[col]
        except:
            print("nodata")
        return None


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        #t = read_csv('trucks.csv', names=['Truck_No'])
        truck_names = ["Trucks"]
        tn = pd.read_csv("trucks.csv", names=truck_names)
        self.t1 = tn.Trucks.to_list()
        # print(self.t1)
        column_names = ["City"]
        cn = pd.read_csv("city_list.csv", names=column_names)
        cities = cn.City.to_list()

        self.completer = QCompleter(cities)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setStyleSheet("background-color: yellow;") 

        self.Year = QtWidgets.QComboBox(self.centralwidget)
        self.Year.setEnabled(True)
        self.Year.setGeometry(QtCore.QRect(30, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        
        self.Year.setFont(font)
        self.Year.setAutoFillBackground(False)
        self.Year.setEditable(False)
        self.Year.setObjectName("Year")
        self.Year.addItem("")
        self.Year.addItem("")
        self.Year.addItem("")
        
        
        
        self.month = QtWidgets.QComboBox(self.centralwidget)
        self.month.setGeometry(QtCore.QRect(180, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.month.setFont(font)
        self.month.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.month.setAutoFillBackground(False)
        self.month.setObjectName("month")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.truck = QtWidgets.QComboBox(self.centralwidget)
        self.truck.setGeometry(QtCore.QRect(370, 20, 131, 51))
        self.truck.setObjectName("truck")
        self.d_click = QtWidgets.QTabWidget(self.centralwidget)
        self.d_click.setGeometry(QtCore.QRect(10, 90, 1321, 481))
        self.d_click.setObjectName("d_click")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.load_name = QtWidgets.QComboBox(self.tab_3)
        self.load_name.setGeometry(QtCore.QRect(0, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.load_name.setFont(font)
        self.load_name.setMaxVisibleItems(6)
        self.load_name.setObjectName("load_name")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")
        self.load_name.addItem("")

        self.dateEdit = QtWidgets.QLineEdit(self.tab_3)
        self.dateEdit.setGeometry(QtCore.QRect(150, 10, 131, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")

        self.frm = QtWidgets.QLineEdit(self.tab_3)
        self.frm.setCompleter(self.completer)

        self.frm.setGeometry(QtCore.QRect(300, 10, 131, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.frm.setFont(font)
        self.frm.setObjectName("frm")

        self.to = QtWidgets.QLineEdit(self.tab_3)
        self.to.setCompleter(self.completer)
        self.to.setGeometry(QtCore.QRect(450, 10, 131, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.to.setFont(font)
        self.to.setObjectName("to")

        self.KM = QtWidgets.QLineEdit(self.tab_3)
        self.KM.setGeometry(QtCore.QRect(600, 10, 118, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.KM.setFont(font)
        self.KM.setObjectName("KM")

        self.arrival = QtWidgets.QLineEdit(self.tab_3)
        self.arrival.setGeometry(QtCore.QRect(740, 10, 118, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.arrival.setFont(font)
        self.arrival.setObjectName("arrival")

        self.unload = QtWidgets.QLineEdit(self.tab_3)
        self.unload.setGeometry(QtCore.QRect(890, 10, 118, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.unload.setFont(font)
        self.unload.setObjectName("unload")

        self.pauch = QtWidgets.QComboBox(self.tab_3)
        self.pauch.setGeometry(QtCore.QRect(1030, 10, 118, 47))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pauch.setFont(font)
        self.pauch.setObjectName("pauch")
        self.pauch.addItem("")
        self.pauch.addItem("")

        self.pauch.addItem("")

        self.enter = QtWidgets.QPushButton(self.tab_3)
        self.enter.setGeometry(QtCore.QRect(1170, 10, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")

        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(10, 90, 1291, 331))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")

        self.d_click.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.a_pay = QtWidgets.QLineEdit(self.tab)
        self.a_pay.setGeometry(QtCore.QRect(300, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.a_pay.setFont(font)
        self.a_pay.setObjectName("a_pay")

        self.a_click = QtWidgets.QPushButton(self.tab)
        self.a_click.setGeometry(QtCore.QRect(440, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a_click.setFont(font)
        self.a_click.setObjectName("a_click")

        self.a_date = QtWidgets.QLineEdit(self.tab)
        self.a_date.setGeometry(QtCore.QRect(20, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.a_date.setFont(font)
        self.a_date.setObjectName("a_date")

        self.a_place = QtWidgets.QLineEdit(self.tab)
        self.a_place.setCompleter(self.completer)
        self.a_place.setGeometry(QtCore.QRect(160, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.a_place.setFont(font)
        self.a_place.setObjectName("a_place")

        self.tableView_5 = QtWidgets.QTableView(self.tab)
        self.tableView_5.setGeometry(QtCore.QRect(700, 60, 591, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableView_5.setFont(font)
        self.tableView_5.setObjectName("tableView_5")

        self.tableView_3 = QtWidgets.QTableView(self.tab)
        self.tableView_3.setGeometry(QtCore.QRect(20, 60, 591, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableView_3.setFont(font)
        self.tableView_3.setObjectName("tableView_3")

        self.d_click.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.d_date = QtWidgets.QLineEdit(self.tab_2)
        self.d_date.setGeometry(QtCore.QRect(20, 9, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d_date.setFont(font)
        self.d_date.setObjectName("d_date")

        self.d_pump = QtWidgets.QLineEdit(self.tab_2)
        self.d_pump.setCompleter(self.completer)
        self.d_pump.setGeometry(QtCore.QRect(160, 9, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d_pump.setFont(font)
        self.d_pump.setObjectName("d_pump")

        self.d_quant = QtWidgets.QLineEdit(self.tab_2)
        self.d_quant.setGeometry(QtCore.QRect(300, 9, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d_quant.setFont(font)
        self.d_quant.setObjectName("d_quant")

        self.d_pay = QtWidgets.QLineEdit(self.tab_2)
        self.d_pay.setGeometry(QtCore.QRect(440, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)

        self.d_pay.setFont(font)
        self.d_pay.setObjectName("d_pay")

        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setGeometry(QtCore.QRect(20, 60, 591, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableView_2.setFont(font)
        self.tableView_2.setObjectName("tableView_2")

        self.tableView_4 = QtWidgets.QTableView(self.tab_2)
        self.tableView_4.setGeometry(QtCore.QRect(700, 60, 591, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableView_4.setFont(font)
        self.tableView_4.setObjectName("tableView_4")

        self.d_click.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.d_click.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.truck_2 = QtWidgets.QComboBox(self.tab_5)
        self.truck_2.setGeometry(QtCore.QRect(20, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.truck_2.setFont(font)
        self.truck_2.setObjectName("truck_2")

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(250, 380, 231, 51))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(960, 380, 231, 51))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(270, 370, 231, 51))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(980, 370, 231, 51))
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1070, 10, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.d_click.addTab(self.tab_5, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.month.setCurrentIndex(0)
        self.d_click.setCurrentIndex(0)
        self.pauch.setCurrentIndex(-1)
        self.load_name.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # calls
        self.Year.currentIndexChanged.connect(self.openClicked)
        self.Year.currentIndexChanged.connect(self.readItems)
        self.truck.currentIndexChanged.connect(self.openClicked)
        self.truck.currentIndexChanged.connect(self.readItems)
        self.month.currentIndexChanged.connect(self.openClicked)
        self.month.currentIndexChanged.connect(self.readItems)
        self.enter.clicked.connect(self.enterClicked)
        self.load_name.currentIndexChanged.connect(self.readItems)
        self.a_click.clicked.connect(self.advance_click)
        self.pushButton.clicked.connect(self.diesel_click)





    def openClicked(self):
        y = self.Year.currentText()
        m = self.month.currentText()
        t = self.truck.currentText()

        db = TinyDB(y+m+t+'.json')
        j = db.table("j_trip")
        a = db.table("advance")
        d = db.table("diesel")

        df = pd.DataFrame.from_dict(j.all())

        self.model = pandasModel(df)
        self.tableView.setModel(self.model)
        try:
            af = pd.DataFrame.from_dict(a.all())
            af["amount"] = pd.to_numeric(af["amount"], downcast="float")

            af.at['Total', 'amount'] = af['amount'].sum()
            af = af.fillna("")
            self.model = pandasModel(af)
            self.tableView_3.setModel(self.model)
            self.tableView_2.setModel(self.model)

            dif = pd.DataFrame.from_dict(d.all())
            dif["rate"] = pd.to_numeric(dif["rate"], downcast="float")
            dif["quantity"] = pd.to_numeric(dif["quantity"], downcast="float")

            dif["amount"] = dif["quantity"] * dif["rate"]
            print(dif)
            dif.at['Total', 'amount'] = dif['amount'].sum()
            dif = dif.fillna("")
            self.model = pandasModel(dif)
            self.tableView_5.setModel(self.model)
            self.tableView_4.setModel(self.model)
        except:
            af = pd.DataFrame.from_dict(a.all())
           
            self.model = pandasModel(af)
            self.tableView_3.setModel(self.model)
            self.tableView_2.setModel(self.model)

            dif = pd.DataFrame.from_dict(d.all())
      
            self.model = pandasModel(dif)
            self.tableView_5.setModel(self.model)
            self.tableView_4.setModel(self.model)
              
    def readItems(self):

        y = self.Year.currentText()
        m = self.month.currentText()
        t = self.truck.currentText()

        db = TinyDB(y+m+t+'.json')
        j = db.table("j_trip")
        a = db.table("advance")
        d = db.table("diesel")

        q = Query()
        if(j.contains(q.load_name == self.load_name.currentText())):
            print("already exist")
            x = j.search(q.load_name == self.load_name.currentText())
            print(x[0]['load_name'])

            self.dateEdit.setText(x[0]["load_date"])
            self.frm.setText(x[0]["frm"])
            self.to.setText(x[0]["too"])
            self.KM.setText(x[0]["km"])
            self.arrival.setText(x[0]["arrival"])
            self.unload.setText(x[0]["unloading"])

            try:
                self.pauch.setCurrentText(x[0]["pauch"])
            except:
                self.pauch.setCurrentText("Pending")

        else:
            print("x")
            self.dateEdit.setText("")
            self.frm.setText("")
            self.to.setText("")
            self.KM.setText("")
            self.arrival.setText("")
            self.unload.setText("")

            try:
                self.pauch.setCurrentText("")
            except:
                # self.dateEdit.setText(j.search(q.name == 'John'))
                self.pauch.setCurrentText("")

        df = pd.DataFrame.from_dict(j.all())

        self.model = pandasModel(df)
        self.tableView.setModel(self.model)

        try:
            af = pd.DataFrame.from_dict(a.all())
            af["amount"] = pd.to_numeric(af["amount"], downcast="float")

            af.at['Total', 'amount'] = af['amount'].sum()
            af = af.fillna("")
            self.model = pandasModel(af)
            self.tableView_3.setModel(self.model)
            self.tableView_2.setModel(self.model)

            dif = pd.DataFrame.from_dict(d.all())
            dif["rate"] = pd.to_numeric(dif["rate"], downcast="float")
            dif["quantity"] = pd.to_numeric(dif["quantity"], downcast="float")

            dif["amount"] = dif["quantity"] * dif["rate"]
            print(dif)
            dif.at['Total', 'amount'] = dif['amount'].sum()
            dif = dif.fillna("")
            self.model = pandasModel(dif)
            self.tableView_5.setModel(self.model)
            self.tableView_4.setModel(self.model)
        except:
            af = pd.DataFrame.from_dict(a.all())
           
            self.model = pandasModel(af)
            self.tableView_3.setModel(self.model)
            self.tableView_2.setModel(self.model)

            dif = pd.DataFrame.from_dict(d.all())
      
            self.model = pandasModel(dif)
            self.tableView_5.setModel(self.model)
            self.tableView_4.setModel(self.model)
            
    def enterClicked(self):

        y = self.Year.currentText()
        m = self.month.currentText()
        t = self.truck.currentText()

        db = TinyDB(y+m+t+'.json')
        j = db.table("j_trip")
        a = db.table("advance")
        d = db.table("diesel")

        q = Query()

        if(j.contains(q.load_name == self.load_name.currentText())):
            print("already exist")
            j.upsert({"load_date": self.dateEdit.text(), "frm": self.frm.text(), "too": self.to.text(), "km": self.KM.text(), "arrival": self.arrival.text(
            ), "unloading": self.unload.text(), "pauch": self.pauch.currentText()}, q.load_name == self.load_name.currentText())

        else:
            j.insert({"load_name": self.load_name.currentText(), "load_date": self.dateEdit.text(), "frm": self.frm.text(), "too": self.to.text(
            ), "km": self.KM.text(), "arrival": self.arrival.text(), "unloading": self.unload.text(), "pauch": self.pauch.currentText()})

        
        #write data to cloud storage
        
        #upload data when internet is connected
        
        
        df = pd.DataFrame.from_dict(j.all())

        self.model = pandasModel(df)
        self.tableView.setModel(self.model)

    def advance_click(self):

        y = self.Year.currentText()
        m = self.month.currentText()
        t = self.truck.currentText()

        db = TinyDB(y+m+t+'.json')
        j = db.table("j_trip")
        a = db.table("advance")
        d = db.table("diesel")

        q = Query()

        a.insert({"date": self.a_date.text(),
                  "place": self.a_place.text(), "amount": self.a_pay.text()})

        af = pd.DataFrame.from_dict(a.all())
        af["amount"] = pd.to_numeric(af["amount"], downcast="float")

        af.at['Total', 'amount'] = af['amount'].sum()
        af = af.fillna("")
        self.model = pandasModel(af)
        self.tableView_3.setModel(self.model)
        self.tableView_2.setModel(self.model)

    def diesel_click(self):

        y = self.Year.currentText()
        m = self.month.currentText()
        t = self.truck.currentText()

        db = TinyDB(y+m+t+'.json')
        j = db.table("j_trip")
        a = db.table("advance")
        d = db.table("diesel")

        q = Query()

        d.insert({"date": self.d_date.text(), "pump": self.d_pump.text(
        ), "quantity": self.d_quant.text(), "rate": self.d_pay.text()})

       
        dif = pd.DataFrame.from_dict(d.all())
        
        
        dif["rate"] = pd.to_numeric(dif["rate"], downcast="float")
        dif["quantity"] = pd.to_numeric(dif["quantity"], downcast="float")

        dif["amount"] = dif["quantity"] * dif["rate"]
        print(dif)
        dif.at['Total', 'amount'] = dif['amount'].sum()
        dif = dif.fillna("")


        self.model = pandasModel(dif)
        self.tableView_5.setModel(self.model)
        self.tableView_4.setModel(self.model)






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Year.setCurrentText(_translate("MainWindow", "2020"))
        self.Year.setItemText(0, _translate("MainWindow", "2020"))
        self.Year.setItemText(1, _translate("MainWindow", "2021"))
        self.Year.setItemText(2, _translate("MainWindow", "2022"))
        self.month.setItemText(0, _translate("MainWindow", "Jan"))
        self.month.setItemText(1, _translate("MainWindow", "Feb"))
        self.month.setItemText(2, _translate("MainWindow", "March"))
        self.month.setItemText(3, _translate("MainWindow", "April"))
        self.month.setItemText(4, _translate("MainWindow", "May"))
        self.month.setItemText(5, _translate("MainWindow", "June"))
        self.month.setItemText(6, _translate("MainWindow", "July"))
        self.month.setItemText(7, _translate("MainWindow", "August"))
        self.month.setItemText(8, _translate("MainWindow", "Sept"))
        self.month.setItemText(9, _translate("MainWindow", "Oct"))
        self.month.setItemText(10, _translate("MainWindow", "Nov"))
        self.month.setItemText(11, _translate("MainWindow", "Dec"))
        self.truck.setAccessibleName(_translate("MainWindow", "Truck"))
        self.enter.setText(_translate("MainWindow", "Submit"))
        self.KM.setPlaceholderText(_translate("MainWindow", "Kilometers"))
        self.to.setPlaceholderText(_translate("MainWindow", "To"))
        self.pauch.setItemText(0, _translate("MainWindow", "Pending"))

        self.pauch.setItemText(1, _translate("MainWindow", "Ok"))
        self.pauch.setItemText(2, _translate("MainWindow", "Damaged"))

        self.unload.setPlaceholderText(
            _translate("MainWindow", "Unloading Date"))
        self.dateEdit.setPlaceholderText(_translate("MainWindow", "Load Date"))
        self.frm.setPlaceholderText(_translate("MainWindow", "_From"))
        self.arrival.setPlaceholderText(
            _translate("MainWindow", "Arrival Date"))
        self.load_name.setItemText(0, _translate("MainWindow", "Bajaj Load"))
        self.load_name.setItemText(1, _translate("MainWindow", "Return 1"))
        self.load_name.setItemText(2, _translate("MainWindow", "Return 2"))
        self.load_name.setItemText(3, _translate("MainWindow", "Return 3"))
        self.load_name.setItemText(4, _translate("MainWindow", "Return 4"))
        self.load_name.setItemText(5, _translate("MainWindow", "Return 5"))
        self.load_name.setItemText(6, _translate("MainWindow", "Return 6"))
        self.load_name.setItemText(7, _translate("MainWindow", "Return 7"))
        self.load_name.setItemText(8, _translate("MainWindow", "Return 8"))
        self.load_name.setItemText(9, _translate("MainWindow", "Return 9"))
        self.load_name.setItemText(10, _translate("MainWindow", "Return 10"))
        self.load_name.setItemText(11, _translate("MainWindow", "Return 11"))
        self.load_name.setItemText(12, _translate("MainWindow", "Return 12"))
        self.load_name.setItemText(13, _translate("MainWindow", "Return 13"))
        self.load_name.setItemText(14, _translate("MainWindow", "Return 14"))
        self.load_name.setItemText(15, _translate("MainWindow", "Return 15"))
        self.d_click.setTabText(self.d_click.indexOf(
            self.tab_3), _translate("MainWindow", "Load Details"))
        self.a_pay.setPlaceholderText(_translate("MainWindow", "Amount"))
        self.a_click.setText(_translate("MainWindow", "Submit"))
        self.a_date.setPlaceholderText(_translate("MainWindow", "Date"))
        self.a_place.setPlaceholderText(_translate("MainWindow", "Place"))
        self.d_click.setTabText(self.d_click.indexOf(
            self.tab), _translate("MainWindow", "Advance"))
        self.d_date.setPlaceholderText(_translate("MainWindow", "Date"))
        self.d_pump.setPlaceholderText(_translate("MainWindow", "Pump"))
        self.d_quant.setPlaceholderText(_translate("MainWindow", "Quantity"))
        self.d_pay.setPlaceholderText(_translate("MainWindow", "Rate"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.d_click.setTabText(self.d_click.indexOf(
            self.tab_2), _translate("MainWindow", "Diesel"))
        self.d_click.setTabText(self.d_click.indexOf(
            self.tab_4), _translate("MainWindow", "Repairing"))
        self.truck_2.setAccessibleName(_translate("MainWindow", "Truck"))
        self.d_click.setTabText(self.d_click.indexOf(
            self.tab_5), _translate("MainWindow", "Documents"))

        self.label_6.setText(_translate("MainWindow", "Viren Logistics"))

        self.truck.addItems(self.t1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
