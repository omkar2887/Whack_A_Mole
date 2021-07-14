import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class Settings_frame(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username1 = str(username)
        loadUi(r"C:\Whack_A_Mole\ui_files\settings_frame.ui", self)
        self.setWindowTitle("Settings")
        self.setFixedSize(800, 800)
        self.username = username
        self.f_profile.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_profile.clicked.connect(self.gotoProfile)

        self.f_resetacc.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_resetacc.clicked.connect(self.reset_account)

        self.f_back.clicked.connect(self.gotomainmenu)

    def gotoProfile(self):
        from profile_settings import Profile_frame
        self.profile_window = Profile_frame(self.username1)
        self.profile_window.show()
        self.close()

    def gotomainmenu(self):
        from Main_menu import Main_menu
        self.main_window = Main_menu(self.username1)
        self.main_window.show()
        self.close()

    def reset_account(self):
        self.reset_window = Reset_Account()
        self.reset_window.show()


class Reset_Account(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\popup_resetaccount.ui", self)
        self.setWindowTitle("Alert")
        self.setFixedSize(500, 200)

        self.f_popup_yes.setStyleSheet(
            "QPushButton{font: 12pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:10px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")

        self.f_popup_no.setStyleSheet(
            "QPushButton{font: 12pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:10px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
