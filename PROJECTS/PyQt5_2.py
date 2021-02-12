#!/usr/bin/python
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QProgressBar
from PyQt5.QtWidgets import QComboBox, QLabel, QStyleFactory
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import  QColorDialog, QCalendarWidget
from PyQt5.QtWidgets import QTextEdit, QInputDialog, QFileDialog, QLineEdit

class Mainwindow(QMainWindow):
    def __init__(self):
        #Window structure set up
        super(Mainwindow, self).__init__()
        self.setWindowTitle("My GUI ")
        self.setGeometry(50,50,500,500)
        self.setWindowTitle('First GUI with PyQt 5')

        #Menu Creation 
        extractAction = QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the App')
        #Image set up for the menu items
        extractAction = QAction(QIcon('Quit.jpg'),'Quit',self)
        extractAction.triggered.connect(self.closeApplication)

        #Main menu creation 
        mainManu = self.menuBar()
        fileMenu = mainManu.addMenu('&File')
        fileMenu.addAction(extractAction)

        #OPen file tab
        openFile = QAction('&OpenFile',self)
        openFile.setShortcut('CTRL+O')
        openFile.setStatusTip('OpenFile')
        openFile.triggered.connect(self.openFile)
        fileMenu.addAction(openFile)


        #Save file 
        saveFile = QAction('&SaveFile',self)
        saveFile.setShortcut('CTRL+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.fileSave)        
        fileMenu.addAction(saveFile)

        self.statusBar()

        
        #Add Toolbar section 
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        #Add Text editior
        openEditor = QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)
        self.toolBar.addAction(openEditor)

        #Addition of Font list
        fontChoice = QAction('Font', self)
        fontChoice.triggered.connect(self.font_Choice)
        fontChoice.setStatusTip('Select Colors')
        self.toolBar.addAction(fontChoice)

        cal = QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)

        self.HomeItems()

    def openFile(self):
        name,_ = QFileDialog.getOpenFileName(self,'OpenFile', options=QFileDialog.DontUseNativeDialog)
        file = open(name,'r')
        self.editor()
        with file:
            text= file.read()
            self.textEdit.setText(text)

    def fileSave(self):
        name,_= QFileDialog.getSaveFileName(self,'SaveFile', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def editor(self):
        self.textEdit =  QTextEdit()
        self.setCentralWidget(self.textEdit)
   
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
        self.styleChoise = QLabel("hey",self)
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

        #Color picker
        color = QColor(0,0,0)
        fontColor = QAction('Colors', self)
        fontColor.triggered.connect(self.colorPicker)
        self.toolBar.addAction(fontColor)

    
    def colorPicker(self):
        color = QColorDialog.getColor()
        self.styleChoise.setStyleSheet('QWidget{background-color:%s}'%color.name())


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