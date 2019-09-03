# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit

from Resources.Tree import *
from Resources.Memory import *

class Ui_Explorer(QtWidgets.QMainWindow):

    def setupUi(self, Explorer): 

        self.backGround = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 33, 33,0.8), stop:1 rgba(13, 115, 119,0.8));"

        Explorer.setObjectName("Explorer")
        Explorer.resize(724, 398)
        Explorer.setMinimumSize(QtCore.QSize(724, 398))
        Explorer.setMaximumSize(QtCore.QSize(724, 398))
        Explorer.setStyleSheet(self.backGround)
        Explorer.setIconSize(QtCore.QSize(24, 24))
        Explorer.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.center(Explorer)
        
        self.centralwidget = QtWidgets.QWidget(Explorer)
        self.centralwidget.setObjectName("centralwidget")

        self.A_NewFile = QtWidgets.QPushButton(self.centralwidget)
        self.A_NewFile.setGeometry(QtCore.QRect(40, 310, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.A_NewFile.setFont(font)
        self.A_NewFile.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.A_NewFile.setObjectName("A_NewFile")
        
        self.Label_A = QtWidgets.QLabel(self.centralwidget)
        self.Label_A.setGeometry(QtCore.QRect(100, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setUnderline(True)
        self.Label_A.setFont(font)
        self.Label_A.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Label_A.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_A.setObjectName("Label_A")
        
        self.B_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.B_Delete.setGeometry(QtCore.QRect(500, 350, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.B_Delete.setFont(font)
        self.B_Delete.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.B_Delete.setObjectName("B_Delete")
        
        self.TreeA = QtWidgets.QListWidget(self.centralwidget)
        self.TreeA.setGeometry(QtCore.QRect(20, 50, 281, 241))
        self.TreeA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TreeA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TreeA.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TreeA.setLineWidth(2)
        self.TreeA.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TreeA.setObjectName("TreeA")
        
        self.TreeB = QtWidgets.QListWidget(self.centralwidget)
        self.TreeB.setGeometry(QtCore.QRect(420, 50, 281, 241))
        self.TreeB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TreeB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TreeB.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TreeB.setObjectName("TreeB")
        
        self.A_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.A_Delete.setGeometry(QtCore.QRect(100, 350, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.A_Delete.setFont(font)
        self.A_Delete.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.A_Delete.setObjectName("A_Delete")
        
        self.A_to_B = QtWidgets.QPushButton(self.centralwidget)
        self.A_to_B.setGeometry(QtCore.QRect(330, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.A_to_B.setFont(font)
        self.A_to_B.setStyleSheet("background-color: rgb(31, 171, 137);")
        self.A_to_B.setObjectName("A_to_B")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255,255,255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.B_NewFolder = QtWidgets.QPushButton(self.centralwidget)
        self.B_NewFolder.setGeometry(QtCore.QRect(570, 310, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.B_NewFolder.setFont(font)
        self.B_NewFolder.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.B_NewFolder.setObjectName("B_NewFolder")
        
        self.B_NewFile = QtWidgets.QPushButton(self.centralwidget)
        self.B_NewFile.setGeometry(QtCore.QRect(440, 310, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.B_NewFile.setFont(font)
        self.B_NewFile.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.B_NewFile.setObjectName("B_NewFile")
        
        self.About = QtWidgets.QPushButton(self.centralwidget)
        self.About.setGeometry(QtCore.QRect(320, 350, 81, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.About.setFont(font)
        self.About.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.About.setObjectName("About")
        
        self.B_to_A = QtWidgets.QPushButton(self.centralwidget)
        self.B_to_A.setGeometry(QtCore.QRect(330, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B_to_A.setFont(font)
        self.B_to_A.setStyleSheet("background-color: rgb(31, 171, 137);")
        self.B_to_A.setObjectName("B_to_A")
        
        self.A_NewFolder = QtWidgets.QPushButton(self.centralwidget)
        self.A_NewFolder.setGeometry(QtCore.QRect(170, 310, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.A_NewFolder.setFont(font)
        self.A_NewFolder.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.A_NewFolder.setObjectName("A_NewFolder")
        
        Explorer.setCentralWidget(self.centralwidget)
        self.retranslateUi(Explorer)

        self.bonsai_A = Tree()
        self.bonsai_B = Tree()


        self.versionLog=(
            """
                0.1.0 - (N-Ary Tree Implemented)\n
                0.2.0 (GUI Implemented)\n
                0.3.0 (Adding Files to Trees)\n
                0.4.0 (Support Copying Files between Trees)\n
                0.5.0 (Matrix To File Implemented)\n
                1.0.0 (Support Browsing through Trees)\n
                1.0.1 (Windows are now centered)\n
                1.0.2 (Version Log Implemented)
            """
        )

        #Señales
        self.A_NewFile.clicked.connect(self.AddFile_A)
        self.B_NewFile.clicked.connect(self.AddFile_B)
        self.A_NewFolder.clicked.connect(self.AddDirectory_A)
        self.B_NewFolder.clicked.connect(self.AddDirectory_B)
        self.A_to_B.clicked.connect(self._copyFromA)
        self.B_to_A.clicked.connect(self._copyFromB)
        self.TreeA.itemDoubleClicked.connect(self.A_Navigator)
        self.TreeB.itemDoubleClicked.connect(self.B_Navigator)
        self.About.clicked.connect(self.A_Save)


        QtCore.QMetaObject.connectSlotsByName(Explorer)

    def AddFile_A(self):
        cuadro = QInputDialog()
        self.centralwidget.setStyleSheet("background-color: rgb(190,190,190);")
        text, okPressed = cuadro.getText(self.centralwidget, "New File","File Name:", QLineEdit.Normal, "")
        self.centralwidget.setStyleSheet(self.backGround)
        if okPressed and text != '':
            file = File_Node(text) 
            verify = self.bonsai_A.addChild(file) 
            if (verify == True):
                if self.bonsai_A.root.name == "/":
                    self.TreeA.clear()
                    childs = self.bonsai_A.root.children
                    self.A_currentChilds(childs.first)
                else:
                    self.TreeA.clear()
                    folder = QtWidgets.QListWidgetItem(None,2)
                    folder.setText(".")
                    back = QtWidgets.QListWidgetItem(None,2)
                    back.setText("..")
                    self.TreeA.addItem(folder)
                    self.TreeA.addItem(back)
                    childs = self.bonsai_A.root.children
                    self.A_currentChilds(childs.first)
            else:
                del file
                self._Warning("File")
            

    def AddFile_B(self):
        cuadro = QInputDialog()
        self.centralwidget.setStyleSheet("background-color: rgb(190, 190, 190);")
        text, okPressed = cuadro.getText(self.centralwidget, "New File","File Name:", QLineEdit.Normal, "")
        self.centralwidget.setStyleSheet(self.backGround)
        if okPressed and text != '':
            file = File_Node(text) 
            verify = self.bonsai_B.addChild(file) 
            if (verify == True):
                item = QtWidgets.QListWidgetItem(None,0)
                icon = QtGui.QIcon() #Instancia de un Icono
                icon.addPixmap(QtGui.QPixmap("Images/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                item.setIcon(icon) 
                item.setText(text) 
                self.TreeB.addItem(item)
            else:
                del file
                self._Warning("File")

    def AddDirectory_A(self):
        cuadro = QInputDialog()
        self.centralwidget.setStyleSheet("background-color: rgb(190, 190, 190);")
        text, okPressed = cuadro.getText(self.centralwidget, "New Folder","Folder Name:", QLineEdit.Normal, "")
        self.centralwidget.setStyleSheet(self.backGround)
        if okPressed and text != '':
            file = Directory_Node(text) 
            verify = self.bonsai_A.addChild(file) 
            if (verify == True):
                if self.bonsai_A.root.name == "/":
                    self.TreeA.clear()
                    childs = self.bonsai_A.root.children
                    self.A_currentChilds(childs.first)
                else:
                    self.TreeA.clear()
                    folder = QtWidgets.QListWidgetItem(None,2)
                    folder.setText(".")
                    back = QtWidgets.QListWidgetItem(None,2)
                    back.setText("..")
                    self.TreeA.addItem(folder)
                    self.TreeA.addItem(back)
                    childs = self.bonsai_A.root.children
                    self.A_currentChilds(childs.first)                 
            else:
                del file
                self._Warning("Folder")


    def AddDirectory_B(self):
        cuadro = QInputDialog()
        self.centralwidget.setStyleSheet("background-color: rgb(190, 190, 190);")
        text, okPressed = cuadro.getText(self.centralwidget, "New Folder","Folder Name:", QLineEdit.Normal, "")
        self.centralwidget.setStyleSheet(self.backGround)
        if okPressed and text != '':
            file = Directory_Node(text) 
            verify = self.bonsai_B.addChild(file) 
            if (verify == True):
                item = QtWidgets.QListWidgetItem(None,1)
                icon = QtGui.QIcon() #Instancia de un Icono
                icon.addPixmap(QtGui.QPixmap("Images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                item.setIcon(icon) 
                item.setText(text)
                self.TreeB.addItem(item)
            else:
                del file
                self._Warning("Folder")

    def _copyFromA(self):
        items = self.TreeA.selectedItems()
        for i in range (len(items)):
            if (items[i].type()==0):
                file = File_Node(items[i].text()) 
                verify = self.bonsai_B.addChild(file) 
                if (verify == True):
                    item = QtWidgets.QListWidgetItem(None,0) 
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("Images/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item.setIcon(icon)
                    item.setText(items[i].text())
                    self.TreeB.addItem(item)
                else:
                    del file
                    self._Warning("File")
            elif (items[i].type()==1):
                file = Directory_Node(items[i].text())
                verify = self.bonsai_B.addChild(file)
                if (verify == True):
                    item = QtWidgets.QListWidgetItem(None,1)
                    icon = QtGui.QIcon() 
                    icon.addPixmap(QtGui.QPixmap("Images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                    item.setIcon(icon) 
                    item.setText(items[i].text())
                    self.TreeB.addItem(item)
                else:
                    del file
                    self._Warning("Folder")

    def _copyFromB(self):
        items = self.TreeB.selectedItems()
        for i in range (len(items)):
            if (items[i].type()==0):
                file = File_Node(items[i].text()) 
                verify = self.bonsai_A.addChild(file)
                if (verify == True):
                    item = QtWidgets.QListWidgetItem(None,0) 
                    icon = QtGui.QIcon() #Instancia de un Icono
                    icon.addPixmap(QtGui.QPixmap("Images/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                    item.setIcon(icon) 
                    item.setText(items[i].text())
                    self.TreeA.addItem(item)
                else:
                    del file
                    self._Warning("File")
            elif (items[i].type()==1):
                file = Directory_Node(items[i].text()) 
                verify = self.bonsai_A.addChild(file) 
                if (verify == True):
                    item = QtWidgets.QListWidgetItem(None,1)
                    icon = QtGui.QIcon() #Instancia de un Icono
                    icon.addPixmap(QtGui.QPixmap("Images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                    item.setIcon(icon) 
                    item.setText(items[i].text())
                    self.TreeA.addItem(item)
                else:
                    del file
                    self._Warning("Folder")

    def A_Navigator(self):
        item = self.TreeA.selectedItems()
        if (item[0].type() == 0):
            print("Es un Archivo, No haré Nada")
        elif (item[0].type() == 1):
            self.bonsai_A.moveTo(item[0].text())
            self.TreeA.clear()
            
            folder = QtWidgets.QListWidgetItem(None,2)
            folder.setText(".")
            back = QtWidgets.QListWidgetItem(None,2)
            back.setText("..")
            self.TreeA.addItem(folder)
            self.TreeA.addItem(back)

            root = self.bonsai_A.root
            if root.children == None:
                root.children = LinkedList()
            current = root.children.first

            self.A_currentChilds(current)
            print("Es un Folder, Limpiare la pantalla y Obtendré la lista con sus hijos")
        elif (item[0].type() == 2 and item[0].text()==".."):
            self.GoBack()
            

    def A_currentChilds(self,current):
        if current is None:
            return True
        else:
            if isinstance(current,Directory_Node):
                text = current.name
                item = QtWidgets.QListWidgetItem(None,1)
                icon = QtGui.QIcon() #Instancia de un Icono
                icon.addPixmap(QtGui.QPixmap("Images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                item.setIcon(icon) 
                item.setText(text)
                self.TreeA.addItem(item)
                self.A_currentChilds(current.next)
            else:
                text = current.name
                item = QtWidgets.QListWidgetItem(None,0) #Creamos una instancia de ListWidgetItem con tipo 0 para diferenciarlos de las carpetas
                icon = QtGui.QIcon() #Instancia de un Icono
                icon.addPixmap(QtGui.QPixmap("Images/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) #Usamos la funcion addPixmap para cargar un mapa de pixeles
                item.setIcon(icon) #Establecemos el icono al nuevo Elemento
                item.setText(text) #Establecemos el nombre del nuevo Elemento
                self.TreeA.addItem(item)
                self.A_currentChilds(current.next)

    def GoBack(self):
        if self.bonsai_A.root.name == "/":
            print("se encuentra en la raiz")
        elif self.bonsai_A.root.parent.name == "/":
            self.TreeA.clear()
            self.bonsai_A.root = self.bonsai_A.root.parent
            childs = self.bonsai_A.root.children
            self.A_currentChilds(childs.first)
        else:
            self.TreeA.clear()
            folder = QtWidgets.QListWidgetItem(None,2)
            folder.setText(".")
            back = QtWidgets.QListWidgetItem(None,2)
            back.setText("..")
            self.TreeA.addItem(folder)
            self.TreeA.addItem(back)
            self.bonsai_A.root = self.bonsai_A.root.parent
            childs = self.bonsai_A.root.children
            self.A_currentChilds(childs.first) 

    def B_Navigator(self):
        item = self.TreeB.selectedItems()
        if (item[0].type() == 0):
            print("Es una carpeta, No haré Nada")
        elif (item[0].type() == 1):
            print("Es un Folder, Limpiare la pantalla y Obtendré la lista con sus hijos")

    def A_Save(self):
        mem = Memory()
        FirstRoot = self.bonsai_A.getFirstRoot(self.bonsai_A.root)
        mem.TreeToMatrix(FirstRoot)
        mem.MatrixToFile()

    def _Warning(self,_type):
        self.centralwidget.setStyleSheet("background-color: rgb(32, 32, 32);")
        infoBox = QtWidgets.QMessageBox(self.centralwidget)
        infoBox.setStyleSheet("background-color: rgb(224, 224, 224);")
        infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        infoBox.setWindowTitle("Warning")
        if (_type=="File"):
            infoBox.setText("The File Already exist in the current Directory")
        else:
            infoBox.setText("The Folder Already exist in the current Directory")

        infoBox.exec_()

        self.centralwidget.setStyleSheet(self.backGround)

    def center(self,object):
        qtRectangle = object.frameGeometry() 
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center() 
        qtRectangle.moveCenter(centerPoint) 
        object.move(qtRectangle.topLeft())

    def showAbout(self):
        infoBox = QtWidgets.QMessageBox(self.centralwidget)
        infoBox.setStyleSheet("background-color: rgb(224, 224, 224);")
        icon = QtGui.QPixmap("Images/IS.png")
        infoBox.setIconPixmap(icon)
        infoBox.setWindowTitle("File Browser")
        font = QtGui.QFont()
        font.setItalic(True)
        font.setWeight(70)
        infoBox.setFont(font)
        infoBox.setDetailedText(self.versionLog)
        infoBox.setText("\n\tVersion 1.0.2\t\n\n\tAlexis Ochoa\n\tMarco Ruíz")

        infoBox.exec_()

    def retranslateUi(self, Explorer):
        _translate = QtCore.QCoreApplication.translate
        Explorer.setWindowTitle(_translate("Explorer", "File Browser"))
        self.A_NewFile.setText(_translate("Explorer", "New File"))
        self.Label_A.setText(_translate("Explorer", "TREE A"))
        self.B_Delete.setText(_translate("Explorer", "Delete"))
        __sortingEnabled = self.TreeA.isSortingEnabled()
        self.TreeA.setSortingEnabled(False)
        self.TreeB.setSortingEnabled(False)
        self.A_Delete.setText(_translate("Explorer", "Delete"))
        self.A_to_B.setText(_translate("Explorer", "→"))
        self.label_2.setText(_translate("Explorer", "TREE B"))
        self.B_NewFolder.setText(_translate("Explorer", "New Folder"))
        self.B_NewFile.setText(_translate("Explorer", "New File"))
        self.About.setText(_translate("Explorer", "About"))
        self.B_to_A.setText(_translate("Explorer", "←"))
        self.A_NewFolder.setText(_translate("Explorer", "New Folder"))