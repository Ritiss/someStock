import tkinter as tk
from tkinter import ttk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
import sys
import mysql.connector
import mysql

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="12345678",
                               database="stock")


def CssLoader(filename):
    with open(filename, 'r') as rd:
        content = rd.read()
        rd.close()
    return content


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Goods")
        self.setGeometry(300, 300, 350, 200)
        self.setObjectName('MainWindow')

        self.setStyleSheet(CssLoader('style.css'))

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Sklad")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Save")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_error)

    def add_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText("You cannot save the database")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)

        error.setDetailedText("We're sorry, but this feature is currently under development.")

        error.exec_()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
