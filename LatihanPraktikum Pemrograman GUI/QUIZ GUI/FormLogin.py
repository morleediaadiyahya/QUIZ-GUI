import sys

from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from FormPendaftaran import*

class MainForm (QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Kuis Pemograman GUI')
        self.Username = QLabel('Username')
        self.Pass = QLabel('Password')
        self.Username1 = QLineEdit()
        self.Pass1 = QLineEdit()
        self.Pass1.setEchoMode(QLineEdit.Password)
        self.button =QPushButton('Login')
        self.button1 =QPushButton('Clear')

        btx =QGridLayout()
        btx.addWidget(self.Username)
        btx.addWidget(self.Username1, 0,1,1,2)
        btx.addWidget(self.Pass)
        btx.addWidget(self.Pass1, 1,1,1,2)
        btx.addWidget(self.button, 2,1)
        btx.addWidget(self.button1, 2,2)
        self.setLayout(btx)

        self.button.clicked.connect(self.buttonClick)
        self.button1.clicked.connect(self.buttonClick1)

    def buttonClick(self):
        user = self.Username1.text()
        psswrd = self.Pass1.text()

        if not user or not psswrd :
            QMessageBox.information(self,'Perhatian!','Username atau Password Harus di Isi')
        else:
            if user == 'melani' and psswrd =='17104010':
                self.form = FormPendaftaran()
                self.form.show()
                self.close()
            else:
                QMessageBox.information(self,'Perhatian!','Username atau password Salah')

    def buttonClick1 (self):
            self.Username1.clear()
            self.Pass1.clear()

if __name__ =='__main__':
        a =QApplication(sys.argv)

        form =MainForm()
        form.show()

        a.exec_()
