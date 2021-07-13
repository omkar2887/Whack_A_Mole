import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class OTP_frame(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"D:\Abhishek\Whack A Mole\ui_files\OTP_frame.ui",self)
        self.setWindowTitle("OTP Verification")
        self.setFixedSize(800,800)
        self.f_sentmail_label.setVisible(False)
        self.f_otp_label.setVisible(False)
        self.f_otp.setVisible(False)
        self.f_submit.setVisible(False)
        self.f_submit.setEnabled(False)

        self.f_sendmail.setStyleSheet("QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_sendmail.clicked.connect(self.send_e)

        self.f_submit.setStyleSheet("QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
    
    def send_e(self):
        import random
        import smtplib
        from email.message import EmailMessage
        global otp

        otp=''.join([str(random.randint(0,9)) for i in range(6)])

        msg=EmailMessage()
        msg['Subject']='Whack A Mole OTP'
        msg['From']='Whack A Mole Game'
        msg['To']='abhishek.otari20@vit.edu'
        msg.set_content("Hello Abhishek, "+otp+" is your one time password to proceed on Whack A Mole game")

        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('gamewhackamole@gmail.com','whackamole@123')
        server.send_message(msg)
        server.quit()

        self.f_sentmail_label.setVisible(True)
        self.f_otp_label.setVisible(True)
        self.f_otp.setVisible(True)
        self.f_submit.setVisible(True)
        self.f_submit.setEnabled(True)
        self.f_sendmail.setVisible(False)
        self.f_sendmail.setEnabled(True)
        self.f_submit.clicked.connect(self.showpass)

    def showpass(self):
        u_otp=self.f_otp.text()
        if u_otp=="":
            self.f_response_otp.setText("*Must enter OTP")
        
        elif u_otp==otp:
            self.f_response_otp.setText("")
            print("Password is shown")
        elif u_otp!=otp:
            self.f_response_otp.setText("")
            print("OTP didn't match")
           


