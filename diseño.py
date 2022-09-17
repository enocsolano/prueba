# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diseño.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: #fff;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.base_datos_todo = QWidget()
        self.base_datos_todo.setObjectName(u"base_datos_todo")
        self.gridLayout = QGridLayout(self.base_datos_todo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.base_datos_todo)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.tableWidget_todo = QTableWidget(self.base_datos_todo)
        if (self.tableWidget_todo.columnCount() < 5):
            self.tableWidget_todo.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_todo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_todo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_todo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_todo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_todo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_todo.rowCount() < 2):
            self.tableWidget_todo.setRowCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_todo.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_todo.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_todo.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_todo.setItem(0, 4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_todo.setItem(1, 1, __qtablewidgetitem9)
        self.tableWidget_todo.setObjectName(u"tableWidget_todo")

        self.gridLayout.addWidget(self.tableWidget_todo, 1, 0, 1, 4)

        self.bt_ir_base_datos_dinamico = QPushButton(self.base_datos_todo)
        self.bt_ir_base_datos_dinamico.setObjectName(u"bt_ir_base_datos_dinamico")

        self.gridLayout.addWidget(self.bt_ir_base_datos_dinamico, 2, 0, 1, 1)

        self.bt_agregar_fila_todo = QPushButton(self.base_datos_todo)
        self.bt_agregar_fila_todo.setObjectName(u"bt_agregar_fila_todo")

        self.gridLayout.addWidget(self.bt_agregar_fila_todo, 2, 1, 1, 1)

        self.bt_eliminar_fila_todo = QPushButton(self.base_datos_todo)
        self.bt_eliminar_fila_todo.setObjectName(u"bt_eliminar_fila_todo")

        self.gridLayout.addWidget(self.bt_eliminar_fila_todo, 2, 2, 1, 1)

        self.bt_refrescar_todo = QPushButton(self.base_datos_todo)
        self.bt_refrescar_todo.setObjectName(u"bt_refrescar_todo")

        self.gridLayout.addWidget(self.bt_refrescar_todo, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.base_datos_todo)
        self.base_datos_dinamico = QWidget()
        self.base_datos_dinamico.setObjectName(u"base_datos_dinamico")
        self.gridLayout_2 = QGridLayout(self.base_datos_dinamico)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.base_datos_dinamico)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.tableWidget_dinamico = QTableWidget(self.base_datos_dinamico)
        if (self.tableWidget_dinamico.columnCount() < 7):
            self.tableWidget_dinamico.setColumnCount(7)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_dinamico.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        self.tableWidget_dinamico.setObjectName(u"tableWidget_dinamico")

        self.gridLayout_2.addWidget(self.tableWidget_dinamico, 1, 0, 1, 4)

        self.bt_ir_base_datos_todo = QPushButton(self.base_datos_dinamico)
        self.bt_ir_base_datos_todo.setObjectName(u"bt_ir_base_datos_todo")

        self.gridLayout_2.addWidget(self.bt_ir_base_datos_todo, 2, 0, 1, 1)

        self.bt_agregar_fila_dinamico = QPushButton(self.base_datos_dinamico)
        self.bt_agregar_fila_dinamico.setObjectName(u"bt_agregar_fila_dinamico")

        self.gridLayout_2.addWidget(self.bt_agregar_fila_dinamico, 2, 1, 1, 1)

        self.bt_eliminar_fila_dinamico = QPushButton(self.base_datos_dinamico)
        self.bt_eliminar_fila_dinamico.setObjectName(u"bt_eliminar_fila_dinamico")

        self.gridLayout_2.addWidget(self.bt_eliminar_fila_dinamico, 2, 2, 1, 1)

        self.bt_refrescar_dinamico = QPushButton(self.base_datos_dinamico)
        self.bt_refrescar_dinamico.setObjectName(u"bt_refrescar_dinamico")

        self.gridLayout_2.addWidget(self.bt_refrescar_dinamico, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.base_datos_dinamico)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BASE TODO", None))
        ___qtablewidgetitem = self.tableWidget_todo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget_todo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget_todo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem3 = self.tableWidget_todo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem4 = self.tableWidget_todo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Calificacion", None));
        ___qtablewidgetitem5 = self.tableWidget_todo.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget_todo.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tableWidget_todo.isSortingEnabled()
        self.tableWidget_todo.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget_todo.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"122", None));
        ___qtablewidgetitem8 = self.tableWidget_todo.item(0, 4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"10.0", None));
        ___qtablewidgetitem9 = self.tableWidget_todo.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"enoc", None));
        self.tableWidget_todo.setSortingEnabled(__sortingEnabled)

        self.bt_ir_base_datos_dinamico.setText(QCoreApplication.translate("MainWindow", u"Ir a base datos dinamico", None))
        self.bt_agregar_fila_todo.setText(QCoreApplication.translate("MainWindow", u"Agregar fila", None))
        self.bt_eliminar_fila_todo.setText(QCoreApplication.translate("MainWindow", u"Eliminar fila", None))
        self.bt_refrescar_todo.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BASE DINAMICA", None))
        ___qtablewidgetitem10 = self.tableWidget_dinamico.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem11 = self.tableWidget_dinamico.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem12 = self.tableWidget_dinamico.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"apellido", None));
        ___qtablewidgetitem13 = self.tableWidget_dinamico.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"edad", None));
        ___qtablewidgetitem14 = self.tableWidget_dinamico.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"calificacion", None));
        ___qtablewidgetitem15 = self.tableWidget_dinamico.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Nombre completo", None));
        ___qtablewidgetitem16 = self.tableWidget_dinamico.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Suma de calificacion y edad", None));
        self.bt_ir_base_datos_todo.setText(QCoreApplication.translate("MainWindow", u"ir a base datos todo", None))
        self.bt_agregar_fila_dinamico.setText(QCoreApplication.translate("MainWindow", u"Agregar fila", None))
        self.bt_eliminar_fila_dinamico.setText(QCoreApplication.translate("MainWindow", u"Eliminar fila", None))
        self.bt_refrescar_dinamico.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
    # retranslateUi

