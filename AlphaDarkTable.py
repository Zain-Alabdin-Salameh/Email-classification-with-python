# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlphaDarkTable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self, MainWindow,datamodel , Accurecy):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 700)
        MainWindow.setStyleSheet("*{\n"
"background:#212121;\n"
"color : white;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1200, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.model=datamodel
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0,1050)
        self.tableView.setStyleSheet("*{\n"
"background:#ffffff;\n"
"color : black;\n"
"width : auto ;\n"
"}\n"
"")
        self.verticalLayout.addWidget(self.tableView)

        self.acc = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.acc.setFont(font)
        self.acc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acc.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.acc.setObjectName("acc")
        self.verticalLayout.addWidget(self.acc)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow,Accurecy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,Accurecy):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Email Classification Project"))
        self.acc.setText(_translate("MainWindow", "Accurecy : "+ str(Accurecy)))

