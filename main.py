import sys  
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QLabel, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QTextEdit, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coach-Fit Bot")
        self.setStyleSheet("background-color: #28282B")

        self.initUI()
        self.showMaximized()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Styling of Coach-fit
        title = QLabel("Coach-Fit", self)
        title.setStyleSheet("color: #FFFFFF; text-align: center;")
        title.setFont(QFont("Poppins", 50))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        #Chatbot history area
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.chat_history.setStyleSheet("""
            QTextEdit {
                background-color: #28282B;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
            }
        """)
        self.chat_history.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        vbox.addWidget(self.chat_history)

        #user input design
        self.textBox = QLineEdit(self)
        self.textBox.setPlaceholderText("What can I help you with?")
        self.textBox.setStyleSheet("""
            QLineEdit {
                padding: 6px 10px;
                color: white;
                min-height: 35px;                   
                border: 2px solid white;
                border-radius: 15px;
                background-color: rgb(255,255,255, 180);
                font-size:14px;
            }
        """)
        self.textBox.returnPressed.connect(self.process_input)  # Enter key 
        self.textBox.setMaximumWidth(600)  # To prevent overgrowth
        

       #send buttoj
        self.send_button = QPushButton("Send", self)
        self.send_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed) 
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #7d807f;
                color: black;
                font-size: 16px;
                min-height: 35px;
                border: 1px solid white;    
                padding: 6px 12px ;
                border-radius: 20px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.send_button.clicked.connect(self.process_input)  # Connect button click to function

        #input
        input_layout = QHBoxLayout()
        input_layout.addStretch(1)  # To center the input field
        input_layout.addWidget(self.textBox, 3)  # Textbox takes more space
        input_layout.addWidget(self.send_button)  # So the "Send" Button takes less space
        input_layout.addStretch(1)  # To center the input field as well

        vbox.addLayout(input_layout)  # Add to main vertical layout

        central_widget.setLayout(vbox)

    def process_input(self):
        """Processes user input and displays chatbot response with chat history."""
        user_input = self.textBox.text().strip()

        if user_input == "":
            return  # No process for empty input

        # Keep user message in chat history
        self.chat_history.append(f"<p style='color: white;'><b>You:</b> {user_input}</p>")

        # Generate bot response
        response = self.get_response(user_input.lower())

        # Keep bot response in chat history
        self.chat_history.append(f"<p style='color: white;'><b>Coach-Fit:</b> {response}</p>")

        # Auto-scroll to the bottom
        self.chat_history.verticalScrollBar().setValue(self.chat_history.verticalScrollBar().maximum())

        # Clear the input field
        self.textBox.clear()

    def get_response(self, user_input):

        """Extracts muscle group from user input and fetches exercises."""

        #  Dictionary that Handles singular/plural/alternative forms of muscle names
        normalization_dict = {
            "bicep": "biceps",
            "tricep": "triceps",
            "leg": "legs",
            "shoulder": "shoulders",
            "ab": "abs",
            "calf": "calves",
            "glute": "glutes",
            "forearm": "forearms"
        }

        # List of valid muscle groups
        muscle_groups = ["biceps", "triceps", "legs", "shoulders", "back", "chest", "abs", "forearms", "glutes", "calves"]

        greetings = ["hello", "hi", "what's up", "good morning", "how you dey?", "how you doing?", "good afternoon", "good evening"]

        # Greeting detection
        for greeting in greetings:
            if greeting in user_input:
                return "Hello! How can I help you with your fitness journey and goals?"

        DISCLAIMER_FOR_PROFESSIONAL_ADVICE = "*Please seek out medical or professional advice before attempting any of the exercises recommended!"

        # Normalize user input for muscle group
        for word in user_input.split():
            # Normalize word if it's in normalization dict
            normalized_word = normalization_dict.get(word, word)  # Default to same word if no mapping
            if normalized_word in muscle_groups:
                # Fetch exercises and append disclaimer
                exercise_response = self.get_exercise(normalized_word)
                return f"{exercise_response}\n\n{DISCLAIMER_FOR_PROFESSIONAL_ADVICE}"

        # Default response if nothing matches
        return "I'm not sure about that. Try asking about a specific muscle group!"

    def get_exercise(self, muscle):
        #Fetches exercises from the database based on the muscle group.
        try:
            conn = sqlite3.connect("Exercise_Data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT exercise FROM Exercise_Data WHERE muscle_group = ?", (muscle,))
            results = cursor.fetchall()
            conn.close()

            if results:
                # Formatting the response as bullet points
                exercises_list = "<br>- " + "<br>- ".join([row[0] for row in results])
                return f"Sure, here are some exercises for you:<br>{exercises_list}"
            else:
                return "I don't have exercises for that muscle group yet."
        except sqlite3.Error as e:
            return f"Database error: {e}"


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
