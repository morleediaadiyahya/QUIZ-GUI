from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class FormPendaftaran(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 300)
        self.move(400, 300)
        self.setWindowTitle('Form Pendaftaran')
        self.label1 = QLabel('<b>Pendaftaran Calon Anggota Avengers</b>')
        self.label2 = QLabel('Nama')
        self.edit1 = QLineEdit()

        self.label3 = QLabel('Jenis Kelamin')
        self.radio1 = QRadioButton()

        self.radio1.setText('Laki-Laki')
        self.radio2 = QRadioButton()
        self.radio2.setText('Perempuan')

        self.label4 = QLabel('Tanggal Lahir')
        self.date = QDateEdit()
        self.date.setDisplayFormat('dd/MM/yyyy')

        self.label5 = QLabel('Hobi')
        self.combo = QComboBox()
        self.combo.addItem('basket')
        self.combo.addItem('sepak bola')
        self.combo.addItem('voli')
        self.combo.addItem('catur')
        self.combo.addItem('lainnya')

        self.label6 = QLabel('Alamat')
        self.text = QTextEdit()

        self.button1 = QPushButton('Submit')
        self.button2 = QPushButton('Cancel')

        layout = QGridLayout()
        layout.addWidget(self.label1,0,1,1,2)
        layout.addWidget(self.label2, 1,0)
        layout.addWidget(self.edit1,  1,1,1,2)
        layout.addWidget(self.label3, 2,0)
        layout.addWidget(self.radio1, 2,1,1,2)
        layout.addWidget(self.radio2, 3,1,1,2)
        layout.addWidget(self.label4, 4,0)
        layout.addWidget(self.date,   4,1,1,2)
        layout.addWidget(self.label5, 5,0)
        layout.addWidget(self.combo,  5,1,1,2)
        layout.addWidget(self.label6, 6,0)
        layout.addWidget(self.text,   6,1,1,2)
        layout.addWidget(self.button1,7,1,1,1)
        layout.addWidget(self.button2,7,2)

        self.setLayout(layout)

        self.button1.clicked.connect(self.button1Click)
        self.button2.clicked.connect(self.button2Click)

    def tes(self):
        if self.radio1.isChecked():
            return "Laki-Laki"
        else:
            return "Perempuan"

    def button1Click(self):
        QMessageBox.information(self, 'Pendaftaran Berhasil',
        'Nama : '+self.edit1.text() +"\n"
        +'Jenis Kelamin : '+ self.tes()+"\n"
        +'Tanggal Lahir : '+ self.date.dateTime().toString()+"\n"
        +'Hobi : '+self.combo.currentText()+"\n"
        +'Alamat : '+self.text.toPlainText())

    def button2Click(self):
        self.close()
