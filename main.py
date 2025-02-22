from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from ui2 import Ui_MainWindow2
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_second_window)
    def open_second_window(self):
        self.second_window = MainWindow(self)
        self.second_window.show()    
class MainWindow(QMainWindow):
    def __init__(self,mainwindow):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.ui.Convert.clicked.connect(self.Convert)
    def Convert(self):
        if self.ui.valute1.currentText()=="Гривні" and self.ui.valute2.currentText()=="Гривні":
            a = int(self.ui.start.text())*1
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Гривні" and self.ui.valute2.currentText()=="Долари":
            a = int(self.ui.start.text())*0.024
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Гривні" and self.ui.valute2.currentText()=="Юані":
            a = int(self.ui.start.text())*0.17
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Гривні" and self.ui.valute2.currentText()=="Злотий":
            a = int(self.ui.start.text())*0.096
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Гривні" and self.ui.valute2.currentText()=="Євро":
            a = int(self.ui.start.text())*0.023
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Гривні" and self.ui.valute2.currentText()=="Фунт":
            a = int(self.ui.start.text())*0.019
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Долари" and self.ui.valute2.currentText()=="Гривні":
            a = int(self.ui.start.text())*41.64
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Долари" and self.ui.valute2.currentText()=="Долари":
            a = int(self.ui.start.text())*1
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Долари" and self.ui.valute2.currentText()=="Юані":
            a = int(self.ui.start.text())*7.25
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Долари" and self.ui.valute2.currentText()=="Євро":
            a = int(self.ui.start.text())*0.96
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Долари" and self.ui.valute2.currentText()=="Фунт":
            a = int(self.ui.start.text())*0.79
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Долари" and self.ui.valute2.currentText()=="Злотий":
            a = int(self.ui.start.text())*3.98
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Юані" and self.ui.valute2.currentText()=="Юані":
            a = int(self.ui.start.text())*1
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Юані" and self.ui.valute2.currentText()=="Долари":
            a = int(self.ui.start.text())*0.14
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Юані" and self.ui.valute2.currentText()=="Гривні":
            a = int(self.ui.start.text())*5.74
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Юані" and self.ui.valute2.currentText()=="Злотий":
            a = int(self.ui.start.text())*0.55
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Юані" and self.ui.valute2.currentText()=="Фунт":
            a = int(self.ui.start.text())*0.11
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Юані" and self.ui.valute2.currentText()=="Євро":
            a = int(self.ui.start.text())*0.13
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Злотий" and self.ui.valute2.currentText()=="Злотий":
            a = int(self.ui.start.text())*1
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Злотий" and self.ui.valute2.currentText()=="Гривні":
            a = int(self.ui.start.text())*10.47
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Злотий" and self.ui.valute2.currentText()=="Долари":
            a = int(self.ui.start.text())*0.25
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Злотий" and self.ui.valute2.currentText()=="Юані":
            a = int(self.ui.start.text())*1.82
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Злотий" and self.ui.valute2.currentText()=="Фунт":
            a = int(self.ui.start.text())*0.2
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Злотий" and self.ui.valute2.currentText()=="Євро":
            a = int(self.ui.start.text())*0.24
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Євро" and self.ui.valute2.currentText()=="Євро":
            a = int(self.ui.start.text())*1
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Євро" and self.ui.valute2.currentText()=="Гривні":
            a = int(self.ui.start.text())*43.57
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Євро" and self.ui.valute2.currentText()=="Долари":
            a = int(self.ui.start.text())*1.05
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Євро" and self.ui.valute2.currentText()=="Юані":
            a = int(self.ui.start.text())*7.59
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Євро" and self.ui.valute2.currentText()=="Злоті":
            a = int(self.ui.start.text())*4.16
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Євро" and self.ui.valute2.currentText()=="Фунт":
            a = int(self.ui.start.text())*0.83
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Фунт" and self.ui.valute2.currentText()=="Фунт":
            a = int(self.ui.start.text())*1
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Фунт" and self.ui.valute2.currentText()=="Гривні":
            a = int(self.ui.start.text())*52.63
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Фунт" and self.ui.valute2.currentText()=="Долари":
            a = int(self.ui.start.text())*1.26
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Фунт" and self.ui.valute2.currentText()=="Злотий":
            a = int(self.ui.start.text())*5.03
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Фунт" and self.ui.valute2.currentText()=="Юані":
            a = int(self.ui.start.text())*9.16
            print(a)
            self.ui.End.setText(str(a))
        if self.ui.valute1.currentText()=="Фунт" and self.ui.valute2.currentText()=="Євро":
            a = int(self.ui.start.text())*1.21
            print(a)
            self.ui.End.setText(str(a))

    
    def money(self):
        if self.mainwindow.ui.valute1.currentText()=="Фунт":
            print(1)
        
app = QApplication([])
ex = Widget()
ex.show()
app.exec()