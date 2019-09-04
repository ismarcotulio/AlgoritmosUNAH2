from Core.Python.GUI.Explorador import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Explorer = QtWidgets.QMainWindow()
    ui = Ui_Explorer()
    ui.setupUi(Explorer)
    Explorer.show()
    run = app.exec_()
    ui.A_Save()
    ui.B_Save()
    sys.exit(run)