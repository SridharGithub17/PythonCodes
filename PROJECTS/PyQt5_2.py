#!/usr/bin/python
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QProgressBar
from PyQt5.QtWidgets import QComboBox, QLabel, QStyleFactory
from PyQt5.QtWidgets import QFontDialog

class Mainwindow(QMainWindow):
    def __init__(self):
        #Window structure set up
        super(Mainwindow, self).__init__()
        self.setWindowTitle("My GUI ")
        self.setGeometry(50,50,300,300)
        self.setWindowTitle('First GUI with PyQt 5')

        #Menu Creation 
        extractAction = QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the App')
        #Image set up for the menu items
        extractAction = QAction(QIcon('Quit.jpg'),'Quit',self)
        extractAction.triggered.connect(self.closeApplication)
        extractAction.triggered.connect(self.closeApplication)
        self.statusBar()

        #Main menu creation 
        mainManu = self.menuBar()
        fileMenu = mainManu.addMenu('&File')
        fileMenu.addAction(extractAction)

        #Add Toolbar section 
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        #Addition of Font list
        fontChoice = QAction('Font', self)
        fontChoice.triggered.connect(self.font_Choice)
        self.toolBar.addAction(fontChoice)

        self.HomeItems()
   
    def font_Choice(self):
       font, valid = QFontDialog.getFont()
       if valid:
           self.styleChoise.setFont(font)


    def HomeItems(self):
        #Button creation and action 
        btn = QPushButton('Quit',self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.closeApplication)
        btn.resize(50,50)
        btn.move(300,300)

        #Checkbox creation
        checkbox = QCheckBox('Enlarge Window',self)
        checkbox.move(0,50)
        checkbox.stateChanged.connect(self.enlargeWindow)

        #Progress Bar for download work
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)
        self.btn = QPushButton('Download', self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.Download)

        #ComboBox  in the home page
        self.styleChoise = QLabel('Windows', self)
        ComboBox = QComboBox(self)
        ComboBox.addItem('motif')
        ComboBox.addItem('Cde')
        ComboBox.addItem('Windows')
        ComboBox.addItem('Plastique')
        ComboBox.addItem('CleanLooks')
        ComboBox.addItem('WindowsVista')
        ComboBox.move(25,250)
        self.styleChoise.move(25,150)
        ComboBox.activated[str].connect(self.style_Choise)

        #QFontDialog box at the home page


    def style_Choise(self,text):
        self.styleChoise.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def Download(self):
        self.completed =0 
        while self.completed < 100:
            self.completed+= 0.0001
            self.progress.setValue(self.completed)

    def enlargeWindow(self, state):
        if state == Qt.Checked:
            self.setGeometry(50,50,500,500)
        else:
            self.setGeometry(50,50,500,300)


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
    window = Mainwindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()