#!/usr/bin/env python3

import pymysql
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QGroupBox,
    QVBoxLayout,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QLabel,
    qApp,
    QAction,
    QTabWidget,
    QTableView
)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)
from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QVariant
)
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQuery,
    QSqlQueryModel
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MySQL Browser")
        self.create_menu_bar()


class DbLoginDialog(QDialog):
    def __init__(self):
        super(DbLoginDialog, self).__init__()
        self.setWindowTitle("Login to MySQL Server")

        self.host = QLineEdit("localhost")
        self.user = QLineEdit("root")
        self.password = QLineEdit()

        form_group_box = QGroupBox("MySQL Server Login Credentials")
        layout = QFormLayout()
        layout.addRow(QLabel("Host:"), self.host)
        layout.addRow(QLabel("User:"), self.user)
        layout.addRow(QLabel("Password:"), self.password)
        form_group_box.setLayout(layout)

        # Consider these 3 lines boiler plate for a standard Ok | Cancel dialog
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(form_group_box)
        vbox_layout.addWidget(button_box)
        self.setLayout(vbox_layout)
        self.password.setFocus()

if __name__=='__main__':
    app = QApplication(sys.argv)
    db_dlg = DbLoginDialog()
    db_dlg.show()

    # This is how you check which button the user used to dismiss the dialog.
    if db_dlg.result() == QDialog.Accepted:
        print("Accepted")
        # connection is global so we can use it in any class, function, or method
        # defined in this module
        global connection
        connection = pymysql.connect(host=db_dlg.host.text(),
                                     user=db_dlg.user.text(),
                                     password=db_dlg.password.text(),
                                     #db='pubs',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute("show databases")
        for row in cursor: print(row)
        main = MainWindow(connection)
        main.show()
    sys.exit(app.exec_())
