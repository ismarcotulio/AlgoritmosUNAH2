# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.Resources.Convertion import *
from Core.Resources.Draw import *
from Core.Resources.MatrixAdyacente import *
from Core.Resources.Floyd import *
from Core.GUI.Table import*

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 438)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 33, 33,0.8), stop:1 rgba(13, 115, 119,0.8));")
        
        self.center(MainWindow)

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
        
        self.destination_Vertex = QtWidgets.QLineEdit(self.centralwidget)
        self.destination_Vertex.setGeometry(QtCore.QRect(430, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destination_Vertex.setFont(font)
        self.destination_Vertex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.destination_Vertex.setObjectName("destination_Vertex")
        
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
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Origin.setFont(font)
        self.Origin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Origin.setStyleSheet("background-color: rgb(255,255,255);")
        self.Origin.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Origin.setAlignment(QtCore.Qt.AlignCenter)
        self.Origin.setObjectName("Origin")
        
        self.destination = QtWidgets.QLabel(self.centralwidget)
        self.destination.setGeometry(QtCore.QRect(300, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.destination.setFont(font)
        self.destination.setStyleSheet("background-color: rgb(255,255,255);")
        self.destination.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.destination.setAlignment(QtCore.Qt.AlignCenter)
        self.destination.setObjectName("destination")
        
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


        self.convertion = Convertion()
        self.dict = {}
        self.matrixAdyacente = MatrixAdyacente()
        self.floyd = AlgoritFloyd()


        self.retranslateUi(MainWindow)
        self.load_File.clicked.connect(self.OpenFile)
        self.generate_Map.clicked.connect(self.Draw_Graph)
        self.generate_Table.clicked.connect(self.GenerateTable)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def OpenFile(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Select a File', '/home', "Tab-Separated Values(*.tsv);;All Files(*)")

        #self.dict = self.convertion.TSVtoDict(file_path[0])
        if file_path[0]:
            f = open(file_path[0],"r")
            content = f.read()
            self.text_Graph.clear()
            self.text_Graph.setPlainText(content)
            print("Se Cargó el Archivo Correctamente")
        else:
            print("Acción Cancelada")

    def Draw_Graph(self):
        content = self.text_Graph.toPlainText()
        self.dict = self.convertion.TSVtoDict(content.strip())
        g = Draw_Graph()
        print(self.dict)
        g.draw(self.dict)

    def GenerateTable(self):
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        matrix = self.matrixAdyacente.MatrixAdyacente(self.dict)
        ui.plainTextEdit.setPlainText(print(self.Floyd.AlgoritFloyd(matrix))
)
        self.center(Form)
        Form.show()
        Form.exec_()

    def center(self,object):
        qtRectangle = object.frameGeometry() 
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center() 
        qtRectangle.moveCenter(centerPoint) 
        object.move(qtRectangle.topLeft())
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Path Finder"))
        self.text_Graph.setPlainText(_translate("MainWindow", "Identifique los vertices, aristas y caracteristicas.\n"
            "Ejemplo:\n"
            "\n"
            "A:\n"
            "\tB:\n"
            "\t\tdistancia:1\n"
            "\t\tanchoDeBanda:1\n"
            "\t\tusuariosConectados:9\n"
            "\t\tcantidadDeTrafico: 2\n"
            "\t\ttipoDeMedio:CAT5\n"
            "\tC:\n"
            "\t\tdistancia:10\n"
            "\t\tanchoDeBanda:7\n"
            "\t\tusuariosConectados:3\n"
            "\t\tcantidadDeTrafico:1\n"
            "\t\ttipoDeMedio:Fibra-Optica\n"
            "B:\n"
            "\tC:\n"
            "\t\tdistancia:10000\n"
            "\t\tanchoDeBanda: 90\n"
            "\t\tusuariosConectados: 7656\n"
            "\t\tcantidadDeTrafico: 87\n"
            "\t\ttipoDeMedio:CAT6"))
        self.load_File.setText(_translate("MainWindow", "Load File"))
        self.generate_Map.setText(_translate("MainWindow", "Generate Map"))
        self.generate_Table.setText(_translate("MainWindow", "Generate Table"))
        self.Origin.setText(_translate("MainWindow", "Origin Vertex"))
        self.destination.setText(_translate("MainWindow", "Destination Vertex"))
        self.label.setText(_translate("MainWindow", "Text Graph"))