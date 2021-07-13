import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
# from level_and_skin import *
from DBhelper import Database


class Main_menu(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username1 = str(username)
        loadUi(r"C:\Whack_A_Mole\ui_files\Main_menu.ui", self)
        self.setWindowTitle("Main Menu")
        self.setFixedSize(800, 800)
        self.f_playgame.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_leaderboard.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_settings.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_settings.clicked.connect(self.set)
        self.f_quit.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_quit.clicked.connect(self.Quit)
        self.f_playgame.clicked.connect(self.level)
        mydatabase = Database()
        result = mydatabase.Query_fetchone("SELECT name FROM users WHERE username = %s", (str(self.username1),))
        print(str(result[0]))
        self.f_response.setText(f"Hii, {str(result[0])}")

    def level(self):
        from level_and_skin import level_skin
        self.xyz=level_skin(str(self.username1))
        self.xyz.show()
        self.close()

    def set(self):
        print(self.username1)
        from settings import Settings_frame
        self.set_window = Settings_frame(self.username1)
        self.set_window.show()
        self.close()

    def Quit(self):
        self.ab = popwindow()
        self.ab.show()


class popwindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\popupwindow.ui", self)
        self.setWindowTitle("Alert")
        self.f_popup_quit.clicked.connect(self.quit)
        self.f_popup_cancel.clicked.connect(self.cancel)

    def quit(self):
        sys.exit()

    def cancel(self):
        self.close()
