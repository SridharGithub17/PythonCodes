#!/usr/bin/python
import sys , os
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt5.QtWidgets import QAction, QMessageBox, QMenu
from PyQt5.QtWidgets import QCheckBox, QProgressBar
from PyQt5.QtWidgets import QComboBox, QLabel, QStyleFactory
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import  QColorDialog, QCalendarWidget
from PyQt5.QtWidgets import QTextEdit, QInputDialog, QFileDialog, QLineEdit
from PyQt5.QtWidgets import QToolBar, QVBoxLayout

class WindowDesign(QMainWindow):
    def __init__(self):
        #Window structure set up
        super(WindowDesign, self).__init__()
        self.setWindowTitle("Mini Calculator")
        # self.setCentralWidget(QLabel("I am the central widget"))
        self.setWindowTitle('Calcualtor')
        self.setFixedWidth(250)
        self.setFixedHeight(250)
        #create menu items
        self._createMenu()
        # self._toolBar()
        #create items in the window body
        self._createSubItems()
    
    def _createSubItems(self):
        btn = QPushButton('  ',self)
        btn.resize(203,45)
        btn.move(20,38)
        btn1 = QPushButton('1',self)
        btn1.resize(40,40)
        btn1.move(20,90)
        btn1.setStatusTip('1')
        btn2 = QPushButton('2',self)
        btn2.resize(40,40)
        btn2.move(65,90)
        btn2.setStatusTip('2')
        btn3 = QPushButton('3',self)
        btn3.resize(40,40)
        btn3.move(105,90)
        btn3.setStatusTip('3')
        btn4 = QPushButton('4',self)
        btn4.resize(40,40)
        btn4.move(145,90)
        btn4.setStatusTip('4')
        btn5 = QPushButton('5',self)
        btn5.resize(40,40)
        btn5.move(185,90)
        btn5.setStatusTip('5')
        btn6 = QPushButton('6',self)
        btn6.resize(40,40)
        btn6.move(20,135)
        btn6.setStatusTip('6')
        btn7 = QPushButton('7',self)
        btn7.resize(40,40)
        btn7.move(65,135)
        btn7.setStatusTip('7')
        btn8 = QPushButton('8',self)
        btn8.resize(40,40)
        btn8.move(105,135)
        btn8.setStatusTip('8')
        btn9 = QPushButton('9',self)
        btn9.resize(40,40)
        btn9.move(145,135)
        btn9.setStatusTip('9')
        btn10 = QPushButton('0',self)
        btn10.resize(40,40)
        btn10.move(185,135)
        btn10.setStatusTip('0')
        btn11 = QPushButton('+',self)
        btn11.resize(40,40)
        btn11.move(20,175)
        btn11.setStatusTip('+')
        btn12 = QPushButton('-',self)
        btn12.resize(40,40)
        btn12.move(65,175)
        btn12.setStatusTip('-')
        btn13 = QPushButton('%',self)
        btn13.resize(40,40)
        btn13.move(105,175)
        btn13.setStatusTip('%')
        btn14 = QPushButton('/',self)
        btn14.resize(40,40)
        btn14.move(145,175)
        btn14.setStatusTip('/')
        btn15 = QPushButton('=',self)
        btn15.resize(40,40)
        btn15.move(185,175)
        btn15.setStatusTip('=')
        #Click activities on the buttons
        # if btn1.clicked.connect(self):
        #     self.btn.setText('1')

            

    def _createMenu(self):
        self.statusBar()
        self.setStatusTip("Mini Calulator")
        menu1 = self.menuBar().addMenu('View')
        #Insert items in the menu
        Standard = QAction('&Standard',self)
        Standard.setShortcut('CTRL+S')
        Standard.setStatusTip('Standard Calculator')
        menu1.addAction(Standard)  
        Standard.triggered.connect(self.callStandard)
        Quit = QAction('&Quit',self) 
        Quit.setShortcut('CTRL+Q')
        Quit.setStatusTip('Exit Application')
        menu1.addAction(Quit)
        Quit.triggered.connect(self.closeApplication)       
        menu2 = self.menuBar().addMenu('Edit')
        Copy = QAction('&Copy',self)
        Copy.setShortcut('CTRL+C')
        Copy.setStatusTip('Copy')
        menu2.addAction(Copy)
        Copy.triggered.connect(self.copyItem)
        Paste = QAction('&Paste',self)
        Paste.setShortcut('CTRL+V')
        Paste.setStatusTip('Copy')
        menu2.addAction(Paste)
        Paste.triggered.connect(self.pasteItem)
        menu3 = self.menuBar().addMenu('Help')
        Help = QAction('&About Calc',self)
        Help.setShortcut('CTRL+H')
        Help.setStatusTip('Help Items')
        menu3.addAction(Help)
        Help.triggered.connect(self.getHelp)
    
    def getHelp(self):
        os.startfile(r'Help.txt')

    def copyItem(self):
        print('Item Copied')
    
    def pasteItem(self):
        print('Paste Item')

    def callStandard(self):
        WindowDesign()

    def closeApplication(self):
        choice = QMessageBox.question(self, 'Message',
                                      "Are you sure to quit?", QMessageBox.Yes , QMessageBox.No)
        if choice == QMessageBox.Yes:
            print('See you again ...')
            sys.exit()
        else:
            pass

def main():
    app = QApplication(sys.argv)
    window= WindowDesign()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()