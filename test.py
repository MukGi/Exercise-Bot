import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class CenteredLabelApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLabel
        label = QLabel("Hello, PyQt5!", self)
        label.setAlignment(Qt.AlignCenter)  # Align text within the label

        # Create a layout and set alignment
        layout = QVBoxLayout()
        layout.addWidget(label, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle("Centered QLabel")
        # self.resize(400, 300)
        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CenteredLabelApp()
    window.show()
    sys.exit(app.exec_())
