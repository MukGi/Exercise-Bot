
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit,
                            QLabel,QWidget,QPushButton, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click Me!",self)
        self.setWindowTitle("Coach-Fit Bot")
        self.setStyleSheet("background-color: #28282B")
        #self.setGeometry(x,y,width,height)
        self.initUI()
        self.showMaximized()



    def initUI(self):
        central_widget =QWidget()
        self.setCentralWidget(central_widget)

        """Coach-Fit Label styling"""
        title = QLabel("Coach-Fit",self)
        title.setStyleSheet("color: #FFFFFF;")
        title.setGeometry(0,0,750,250)
        title.setFont(QFont("Poppins", 50))
        grid = QGridLayout()
        grid.addWidget(title,0,0)
    

def main():
    app =  QApplication(sys.argv)
    window  = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

