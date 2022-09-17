import sys
from diseño import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog, QListWidget, QLabel, QStackedWidget, QHBoxLayout, QApplication, QTableWidgetItem
from codigo.conector import *


class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        #CREAMOS ESTE OBJETO/PROPIEDAD UI PARA ACCEDER A LOS DIFERENTES COMPONENTES DEL DISEÑO
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.bt_ir_base_datos_dinamico.clicked.connect(lambda: self.ui.stackedWidget(self.ui.base_datos_dinamico))
        self.ui.bt_ir_base_datos_dinamico.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.base_datos_dinamico))
        self.ui.bt_ir_base_datos_todo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.base_datos_todo))

        self.ui.bt_agregar_fila_dinamico.clicked.connect(self._addRow)
        self.ui.bt_eliminar_fila_dinamico.clicked.connect(self._quitarRow)
        self.removerRowCero()

    def removerRowCero(self):
        self.ui.tableWidget_dinamico.removeRow(0)

    def _quitarRow(self):
        self.ui.tableWidget_dinamico.removeRow(0)

    def _addRow(self):
        self.ui.tableWidget_dinamico.insertRow(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
