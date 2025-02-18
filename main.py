import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QLabel, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click Me!", self)
        self.setWindowTitle("Coach-Fit Bot")
        self.setStyleSheet("background-color: #28282B")

        self.initUI()
        self.showMaximized()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        """ Coach-Fit Label styling """
        title = QLabel("Coach-Fit", self)
        title.setStyleSheet("color: #FFFFFF; text-align: center;")
        title.setGeometry(0, 0, 350, 93)
        title.setFont(QFont("Poppins", 50))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        """ Center Border Design """
        self.border = QFrame(self)
        self.border.setFrameShape(QFrame.Shape.Box)  # Updated for PyQt6
        self.border.setStyleSheet("""
            QFrame {
                background-color: white;
                padding: 10px;
                width: 629px;
                height: 600px;
            }
        """)

        panelDec = QHBoxLayout(self.border)
        panelDec.addWidget(self.border, alignment=Qt.AlignmentFlag.AlignCenter)

        """ User Input Design """
        self.textBox = QLineEdit(self)
        self.textBox.setPlaceholderText("Enter text here")
        self.textBox.setStyleSheet("""
            QLineEdit {
                padding: 20px 10px;
                width: 350px;
                height: 26px;
                color: white;
                margin-bottom: 30px;
                border: 3px solid white;
                border-radius: 10px;
                background-color: rgb(255,255,255, 180);
            }
        """)

        tbox = QHBoxLayout()
        tbox.addWidget(self.textBox, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        vbox.addLayout(tbox)
        vbox.addLayout(panelDec)
        central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # Updated for PyQt6

if __name__ == "__main__":
    main()
