#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys
 

class MainWindow(QMainWindow):
    def __init__(self):
        #Window structure set up
        super(MainWindow, self).__init__()
        self.setWindowTitle("Contact List Manager")
        # self.setCentralWidget(QLabel("I am the central widget"))
        self.setWindowTitle('Contacts')
        # self.setWindowIcon(QIcon('ContactList2.png'))
        self.setFixedWidth(500)
        self.setFixedHeight(600)
        self.label = QLabel(self)
        self.label.resize(500,600)
        # self.label.setStyleSheet("background-image : url(ContactList1.png);\
                                        #   border   : 2px solid blue")
        self.label.setStyleSheet("background-color : grey;\
                                          border   : 2px solid blue")
        self._ObjectsTest()

    def _ObjectsTest(self):
        b = QLabel()
        b.setText("Sridhar Das")
        b.move(50,20)



def main():
    app= QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()


