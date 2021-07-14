import sys
from PyQt5.QtWidgets import QButtonGroup, QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


# make class variables (add all variables)

# from gameframe import score,t,countdown_time,start ,mouseflag,cursorflag
# score = 0
# t = 15
# countdown_time = 3
# start = False
# mouseflag=cursorflag=0

class Result(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\result.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Result")

        self.f_playagain.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_playagain.clicked.connect(self.goto_playagain)

        self.f_next.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_next.clicked.connect(self.goto_leaderboard)

        self.f_quit.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_quit.clicked.connect(self.goto_quit)

        from gameframe import score
        self.f_score.setText(str(score))

        # if score >= 10:
        #     self.result_label.setText("Well done")
        # else:
        #     self.result_label.setText("Can do better")

    def goto_playagain(self):
        from gameframe import GameFrame
        self.z = GameFrame()
        self.z.show()
        self.close()

    def goto_leaderboard(self):
        pass

    def goto_quit(self):
        from Main_menu import popwindow
        self.a_window = popwindow()
        self.a_window.show()


