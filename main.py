
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit,
                            QLabel,QWidget,QPushButton, QGridLayout, QVBoxLayout,QHBoxLayout,
                            QFrame)
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
        title.setStyleSheet("color: #FFFFFF;"
                            "text-align: center")
        title.setGeometry(0,0,350,93)
        title.setFont(QFont("Poppins", 50))
        title.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(title, alignment=Qt.AlignCenter|Qt.AlignTop)
        """Center Border Design - In progress"""
        # border =  QFrame()
        # border.setFrameShape(QFrame.Box)
        # border.setStyleSheet("background-color: lightgray; padding: 10px;")

        # layout = QVBoxLayout(border)
        # layout.addWidget(QLabel("Label inside QFrame"))

        """UserInput design"""
        self.textBox = QLineEdit("Enter text here", self)
        self.textBox.setGeometry(0,0,517,200)
        self.textBox.setStyleSheet("""
        
        
        """)

        tbox = QHBoxLayout()
        tbox.addWidget(self.textBox, alignment = Qt.AlignBottom|Qt.AlignCenter)

        vbox.addLayout(tbox)
        central_widget.setLayout(vbox)
        

        
        

    

    

def main():
    app =  QApplication(sys.argv)
    window  = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

