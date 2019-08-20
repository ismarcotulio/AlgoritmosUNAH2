# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Item import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 374)
        self.TreeA = QtWidgets.QListWidget(Form)
        self.TreeA.setGeometry(QtCore.QRect(30, 20, 256, 192))
        self.TreeA.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TreeA.setObjectName("TreeA")
        item = QtWidgets.QListWidgetItem()
        self.TreeA.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TreeA.addItem(item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.copiar = QtWidgets.QPushButton(Form)
        self.copiar.setGeometry(QtCore.QRect(280, 230, 89, 25))
        self.copiar.setObjectName("copiar")
        self.TreeB = QtWidgets.QListWidget(Form)
        self.TreeB.setGeometry(QtCore.QRect(310, 20, 256, 192))
        self.TreeB.setObjectName("TreeB")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self._add)
        self.copiar.clicked.connect(self._copy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def _add(self):
        obj = Item()
        self.TreeA.addItem(obj.nombre)

    def _copy(self):
        items = self.TreeA.selectedItems()
        for i in range (len(items)):
            self.TreeB.addItem(items[i].text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.TreeA.isSortingEnabled()
        self.TreeA.setSortingEnabled(False)
        item = self.TreeA.item(0)
        item.setText(_translate("Form", "."))
        item = self.TreeA.item(1)
        item.setText(_translate("Form", ".."))
        self.TreeA.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "Agregar"))
        self.copiar.setText(_translate("Form", "Copiar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
