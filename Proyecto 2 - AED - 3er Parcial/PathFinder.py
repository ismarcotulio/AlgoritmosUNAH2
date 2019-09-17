# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PathFinder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 438)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 33, 33,0.8), stop:1 rgba(13, 115, 119,0.8));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_Graph = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_Graph.setGeometry(QtCore.QRect(20, 50, 531, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_Graph.setFont(font)
        self.text_Graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_Graph.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.text_Graph.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.text_Graph.setObjectName("text_Graph")
        self.origin_Vertex = QtWidgets.QLineEdit(self.centralwidget)
        self.origin_Vertex.setGeometry(QtCore.QRect(200, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.origin_Vertex.setFont(font)
        self.origin_Vertex.setStyleSheet("background-color: rgb(253, 246, 227);")
        self.origin_Vertex.setObjectName("origin_Vertex")
        self.destiny_Vertex = QtWidgets.QLineEdit(self.centralwidget)
        self.destiny_Vertex.setGeometry(QtCore.QRect(430, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destiny_Vertex.setFont(font)
        self.destiny_Vertex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.destiny_Vertex.setObjectName("destiny_Vertex")
        self.load_File = QtWidgets.QPushButton(self.centralwidget)
        self.load_File.setGeometry(QtCore.QRect(110, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.load_File.setFont(font)
        self.load_File.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.load_File.setObjectName("load_File")
        self.generate_Map = QtWidgets.QPushButton(self.centralwidget)
        self.generate_Map.setGeometry(QtCore.QRect(330, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.generate_Map.setFont(font)
        self.generate_Map.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.generate_Map.setObjectName("generate_Map")
        self.generate_Table = QtWidgets.QPushButton(self.centralwidget)
        self.generate_Table.setGeometry(QtCore.QRect(220, 390, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.generate_Table.setFont(font)
        self.generate_Table.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.generate_Table.setObjectName("generate_Table")
        self.Origin = QtWidgets.QLabel(self.centralwidget)
        self.Origin.setGeometry(QtCore.QRect(70, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Origin.setFont(font)
        self.Origin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Origin.setStyleSheet("background-color: rgb(255,255,255);")
        self.Origin.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Origin.setAlignment(QtCore.Qt.AlignCenter)
        self.Origin.setObjectName("Origin")
        self.Destiny = QtWidgets.QLabel(self.centralwidget)
        self.Destiny.setGeometry(QtCore.QRect(300, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Destiny.setFont(font)
        self.Destiny.setStyleSheet("background-color: rgb(255,255,255);")
        self.Destiny.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Destiny.setAlignment(QtCore.Qt.AlignCenter)
        self.Destiny.setObjectName("Destiny")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(215, 11, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Path Finder"))
        self.text_Graph.setPlainText(_translate("MainWindow", "Identifique los vertices, aristas y caracteristicas.\n"
"Ejemplo:\n"
"\n"
"A:\n"
"    B:\n"
"        distancia:1\n"
"        anchoDeBanda:1\n"
"        usuariosConectados:9\n"
"        cantidadDeTrafico: 2\n"
"        tipoDeMedio:CAT5\n"
"    C:\n"
"        distancia:10\n"
"        anchoDeBanda:7\n"
"        usuariosConectados:3\n"
"        cantidadDeTrafico:1\n"
"        tipoDeMedio:Fibra-Optica\n"
"B:\n"
"    C:\n"
"        distancia:10000\n"
"        anchoDeBanda: 90\n"
"        usuariosConectados: 7656\n"
"        cantidadDeTrafico: 87\n"
"        tipoDeMedio:CAT6"))
        self.load_File.setText(_translate("MainWindow", "Load File"))
        self.generate_Map.setText(_translate("MainWindow", "Generate Map"))
        self.generate_Table.setText(_translate("MainWindow", "Generate Table"))
        self.Origin.setText(_translate("MainWindow", "Origin Vertex"))
        self.Destiny.setText(_translate("MainWindow", "Destiny Vertex"))
        self.label.setText(_translate("MainWindow", "Text Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
