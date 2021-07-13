import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class Startwindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\startwindow.ui", self)
        # loadUi(
        #     r"..\ui_files\startwindow.ui",
        #     self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Whack A Mole Game")

    def mousePressEvent(self, click):
        from login_signup_forgot_pass import Login
        if click.button() == Qt.LeftButton:
            self.w = Login()
            self.w.show()
            self.close()


app = QApplication(sys.argv)
window = Startwindow()
window.show()
sys.exit(app.exec_())
