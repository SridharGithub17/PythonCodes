#!/sh/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5.QtCore import Qt

# def MainWindow():
#     # .setWindowTitle(" First GUI App ")
#     Label = QLabel("This is my first GUI program ")
#     Label.setAlignment(Qt.AlignCenter)
#     # .setCentralWidget(Label)

def main():
    #sys.argv for command line arguments
    app = QApplication(sys.argv)

    window = QWidget()
    window.setGeometry(50, 50, 500, 300)
    window.setWindowTitle('pyQt Tuts')

    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
