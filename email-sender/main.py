from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
from src.python_app import send_email


class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("main.ui", self)

        self.emailButton.clicked.connect(self.send_email)

    def send_email(self):
        if self.lineEdit_2.text():
            send_email(to_line=self.lineEdit_2.text(),
                       subject_line=self.lineEdit_3.text(),
                       body_text=self.textEdit.toPlainText())
        else:
            message = QMessageBox()
            message.setText("Invalid Email")
            message.setWindowTitle("Error!")
            message.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()
