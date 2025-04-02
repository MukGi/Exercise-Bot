import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QLabel, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# Import functions from coach.py
from coach import get_bot_response, get_response_dict

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coach-Fit Bot")
        self.setStyleSheet("background-color: #28282B")
        self.initUI()
        self.showMaximized()
        self.response_dict = get_response_dict()  # Initialize response dictionary

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        title = QLabel("Coach-Fit", self)
        title.setStyleSheet("color: #FFFFFF; text-align: center;")
        title.setFont(QFont("Poppins", 50))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.chat_history.setStyleSheet("""
            QTextEdit {
                background-color: #48484E;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
            }
        """)

        vbox.addWidget(self.chat_history, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.textBox = QLineEdit(self)
        self.textBox.setPlaceholderText("What can I help you with?")
        self.textBox.setStyleSheet("""
            QLineEdit {
                padding: 20px 10px;
                color: white;
                border: 3px solid white;
                border-radius: 10px;
                background-color: rgb(255,255,255, 180);
            }
        """)
        self.textBox.returnPressed.connect(self.process_input)

        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #7d807f;
                color: black;
                font-size: 16px;
                min-height: 35px;
                border: 1px solid white;    
                padding: 6px 12px ;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.send_button.clicked.connect(self.process_input)

        input_layout = QHBoxLayout()
        input_layout.addStretch(1)
        input_layout.addWidget(self.textBox, 3)
        input_layout.addWidget(self.send_button)
        input_layout.addStretch(1)

        vbox.addLayout(input_layout)
        central_widget.setLayout(vbox)

    def process_input(self):
        """Processes user input and displays chatbot response."""
        user_input = self.textBox.text().strip()

        if not user_input:
            return

        self.chat_history.append(f"<p style='color: white;'><b>You:</b> {user_input}</p>")

        response = get_bot_response(user_input.lower(), self.response_dict)

        self.chat_history.append(f"<p style='color: white;'><b>Coach-Fit:</b> {response}</p>")

        self.chat_history.verticalScrollBar().setValue(self.chat_history.verticalScrollBar().maximum())

        self.textBox.clear()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
