from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidget, QTableWidgetItem, QTableView
import sys
import sqlite3


class Ui_MainWindow(object):
    def loadData(self):
        connection = sqlite3.connect('stock.db')
        query = "SELECT * FROM box"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 130, 901, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(280, 670, 181, 51))
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.loadData)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(590, 670, 181, 51))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.add_error)
        self.main_text = QtWidgets.QLabel(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(390, 50, 291, 41))
        self.main_text.setObjectName("main_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))
        self.main_text.setText(_translate("MainWindow", "Товары на складе"))

    def add_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText("You cannot save the database")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)

        error.setDetailedText("We're sorry, but this feature is currently under development.")

        error.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
