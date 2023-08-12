# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Conversor(object):
    def setupUi(self, Conversor):
        Conversor.setObjectName("Conversor")
        Conversor.resize(459, 202)
        self.centralwidget = QtWidgets.QWidget(Conversor)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(260, 120, 75, 23))
        self.botao_sair.setObjectName("botao_sair")
        self.botao_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_converter.setGeometry(QtCore.QRect(60, 120, 75, 23))
        self.botao_converter.setObjectName("botao_converter")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 201, 20))
        self.label.setObjectName("label")
        self.entrada_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_temp.setGeometry(QtCore.QRect(260, 40, 113, 20))
        self.entrada_temp.setObjectName("entrada_temp")
        Conversor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Conversor)
        self.statusbar.setObjectName("statusbar")
        Conversor.setStatusBar(self.statusbar)

        self.retranslateUi(Conversor)
        self.botao_sair.clicked.connect(Conversor.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Conversor)

        self.botao_converter.clicked.connect(self.converter)

    def converter(self):
        temp = int(self.entrada_temp.text())
        temp = (temp-32) * 5/9

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso")
        msg.setText("Resultado: " + str(temp) + "°C")
        msg.exec()

    def retranslateUi(self, Conversor):
        _translate = QtCore.QCoreApplication.translate
        Conversor.setWindowTitle(_translate("Conversor", "Conversor"))
        self.botao_sair.setText(_translate("Conversor", "Sair"))
        self.botao_converter.setText(_translate("Conversor", "Converter"))
        self.label.setText(_translate("Conversor", "Conversor de temperatura °F to °C"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Conversor()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())