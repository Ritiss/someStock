from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidget, QTableWidgetItem, QTableView
import sys
import sqlite3


def CssLoader(filename):
    with open(filename, 'r') as rd:
        content = rd.read()
        rd.close()
    return content


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("stock.db")
    con.open()


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("Goods")
        self.setGeometry(50, 50, 1800, 1000)
        self.setObjectName('MainWindow')

        self.setStyleSheet(CssLoader('style.css'))

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Sklad ebani")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(10, 380)
        self.btn.setText("Save")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_error)

        self.btn_open_dialog = QtWidgets.QPushButton(self)
        self.btn_open_dialog.setText("Add")
        self.btn_open_dialog.move(10, 350)
        self.btn_open_dialog.setFixedWidth(200)
        self.btn.clicked.connect(self.add_btn)

        self.btn_edit_dialog = QtWidgets.QPushButton(self)
        self.btn_edit_dialog.setText("Edit")
        self.btn_edit_dialog.setFixedWidth(200)

        self.btn_delete_dialog = QtWidgets.QPushButton(self)
        self.btn_delete_dialog.setText("Delete")
        self.btn_delete_dialog.setFixedWidth(200)

        self.model = QSqlTableModel(self)
        self.model.setTable("box")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "id")
        self.model.setHeaderData(1, Qt.Horizontal, "title")
        self.model.setHeaderData(2, Qt.Horizontal, "amount")
        self.model.setHeaderData(3, Qt.Horizontal, "price")
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)

    def add_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText("You cannot save the database")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)

        error.setDetailedText("We're sorry, but this feature is currently under development.")

        error.exec_()

    def add_btn(self):
        title = self.lineEdit.text()
        amount = self.lineEdit_2.text()
        price = self.lineEdit_3.text()
        print(title, amount, price)
        insert = (title, amount, price)

        with sqlite3.connect('stock.db') as db:
            cur = db.cursor()
            query = """INSERT INTO box (title, amount, price) VALUES (?, ?, ?)"""
            cur.execute(query, insert)
            db.commit()


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("stock.db")
    if not con.open():
        QMessageBox.critical(
            None,
            "Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)

    window = Window()
    window.show()

    sys.exit(app.exec_())
