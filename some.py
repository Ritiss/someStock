from PyQt5 import QtSql, QtGui


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('stock.db')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery()

    query.exec_("create table box(id int primary key auto_increment, title varchar(255), amount int, price INT)")

    query.exec_("insert into box values(1, 'Шина летняя Bridgestone Ecopia EP150 175/65 R14 82H', 24, 2600)")
    query.exec_("insert into box values(2, 'Свеча зажигания для а/м ВАЗ 08-09 (14R-7DU) Z-20', 100, 250)")
    query.exec_("insert into box values(3, 'Диск штампованный R16 5.5J 6x170/130 ET105', 8, 4000)")
    query.exec_("insert into box values(4, 'Насос топливный электрический для а/м ВАЗ 21044', 2, 740)")
    query.exec_("insert into box values(5, 'Регулятор холостого хода для а/м ВАЗ 2108, 2115', 1, 600)")
    return True


if __name__ == '__main__':
    import sys

    app = QtGui.QGuiApplication(sys.argv)
    createDB()
