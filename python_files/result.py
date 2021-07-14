import sys
from PyQt5.QtWidgets import QButtonGroup, QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from DBhelper import Database


# make class variables (add all variables)

# from gameframe import score,t,countdown_time,start ,mouseflag,cursorflag
# score = 0
# t = 15
# countdown_time = 3
# start = False
# mouseflag=cursorflag=0

class Result(QDialog):
    def __init__(self, username):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\result.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Result")
        self.username1 = str(username)
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
        self.now_score = score
        self.f_score.setText(str(score))
        mydatabase = Database()
        mydatabase.Query_insert(
            "INSERT INTO highscores (username, score, date, time) VALUES (%s, %s, date(sysdate()), time(sysdate()))",
            (str(self.username1), int(score)))
        self.level_and_skin_update()
        # if score >= 10:
        #     self.result_label.setText("Well done")
        # else:
        #     self.result_label.setText("Can do better")

    def goto_playagain(self):
        from gameframe import GameFrame
        self.z = GameFrame(self.username1)
        self.z.show()
        self.close()

    def goto_leaderboard(self):
        pass

    def goto_quit(self):
        from Main_menu import popwindow
        self.a_window = popwindow()
        self.a_window.show()

    def level_and_skin_update(self):
        mydatabase = Database()
        if int(self.now_score) >= 50:
            mydatabase.Query_update("UPDATE levels_and_skins SET e2 = %s, s2 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 100:
            mydatabase.Query_update("UPDATE levels_and_skins SET e3 = %s, s3 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 150:
            mydatabase.Query_update("UPDATE levels_and_skins SET m1 = %s, s4 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 200:
            mydatabase.Query_update("UPDATE levels_and_skins SET m2 = %s, s5 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 250:
            mydatabase.Query_update("UPDATE levels_and_skins SET m3 = %s, s6 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 300:
            mydatabase.Query_update("UPDATE levels_and_skins SET h1 = %s, s7 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 350:
            mydatabase.Query_update("UPDATE levels_and_skins SET h2 = %s, s8 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 400:
            mydatabase.Query_update("UPDATE levels_and_skins SET h3 = %s, s9 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
