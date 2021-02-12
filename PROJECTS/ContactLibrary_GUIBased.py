#!/usr/bin/python
import sys, webbrowser, os
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
from PyQt5.QtWidgets import QFrame, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        #Window structure set up
        super(MainWindow, self).__init__()
        self.setWindowTitle("Contact List Manager")
        # self.setCentralWidget(QLabel("I am the central widget"))
        self.setWindowTitle('Contacts')
        self.setWindowIcon(QIcon('ContactList2.png'))
        self.setFixedWidth(500)
        self.setFixedHeight(600)
        self.label = QLabel(self)
        self.label.resize(500,600)
        # self.label.setStyleSheet("background-image : url(ContactList1.png);\
                                        #   border   : 2px solid blue")
        self.label.setStyleSheet("background-color : blue;\
                                          border   : 2px solid blue")
        self._setMenuItems()
        self._setWindowObjects()
        
    def _setMenuItems(self):
        self.statusBar()
        self.setStatusTip("Contact List")
        menu1 = self.menuBar().addMenu('Contact')
        #Insert items in the menu
        New = QAction('&New',self)
        New.setShortcut('CTRL+N')
        New.setStatusTip('New Contact')
        menu1.addAction(New)
        New.triggered.connect(self.addNewContact)
        Update = QAction('&Update',self) 
        Update.setShortcut('CTRL+U')
        Update.setStatusTip('Update Contact')
        menu1.addAction(Update)
        Update.triggered.connect(self.updateContact)  
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
        #Open file in notepad as it is
        os.startfile(r'Help.txt')
        #Open file in browser
        # webbrowser.open(os.getcwd() + "C:/Users/Sridhar/Desktop/Project doc/PYTHON/GIT/PythonCodes/PROJECTS/Help.txt")
        #Open with adhoc defined editor
        # name,_ = QFileDialog.getOpenFileName(self,'OpenFile', options=QFileDialog.DontUseNativeDialog)
        # file = open("Help.txt",'r')
        # self.editor()
        # with file:
        #     text= file.read()
        #     self.textEdit.setText(text)
        # file.close

    def copyItem(self):
        print('Item Copied')
    
    def pasteItem(self):
        print('Paste Item')

    def addNewContact(self):
        print('Add New')

    def updateContact(self):
        print('Update contact')

    def closeApplication(self):
        choice = QMessageBox.question(self, 'Message',
                                      "Are you sure to quit?", QMessageBox.Yes , QMessageBox.No)
        if choice == QMessageBox.Yes:
            print('See you again ...')
            sys.exit()
        else:
            pass
    
    def _setWindowObjects(self):
        #ComboBox  in the home page
        #Window size 500,600
        self.styleChoise = QLabel("January",self)
        self.styleChoise.setStyleSheet("background-color: red")
        self.resize(20,40)
        self.styleChoise.move(280,40) #Position
        ComboBox = QComboBox(self)
        ComboBox.addItem('January')
        ComboBox.addItem('February')
        ComboBox.addItem('March')
        ComboBox.addItem('April')
        ComboBox.addItem('May')
        ComboBox.addItem('June')
        ComboBox.addItem('July')
        ComboBox.addItem('August')
        ComboBox.addItem('September')
        ComboBox.addItem('October')
        ComboBox.addItem('November')
        ComboBox.addItem('December')
        ComboBox.move(20,40)  #size
        ComboBox.activated[str].connect(self.style_Choise)
        #Frame for the box
        hbox = QHBoxLayout()
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(10)
        frame.setMidLineWidth(10)
        frame.resize(200, 400)
        frame.move(280,90)
        frame.setStyleSheet(".QFrame { background-color : white } ")
        hbox.addWidget(frame)
        #Buttons
        btn1 = QPushButton('AddNew',self)
        btn1.resize(75,50)
        btn1.move(20,90)
        btn1.setStatusTip('AddNew')
        btn2 = QPushButton('Edit',self)
        btn2.resize(75,50)
        btn2.move(100,90)
        btn2.setStatusTip('Edit')
        btn3 = QPushButton('View',self)
        btn3.resize(75,50)
        btn3.move(175,90) 
        btn3.setStatusTip('View') ###
        btn4 = QPushButton('Delete',self)
        btn4.resize(75,50)
        btn4.move(20,150)
        btn4.setStatusTip('Delete')
        btn5 = QPushButton('ShowAll',self)
        btn5.resize(75,50)
        btn5.move(100,150)
        btn5.setStatusTip('ShowAll')
        btn6 = QPushButton('RemoveDups',self)
        btn6.resize(75,50)
        btn6.move(175,150) 
        btn6.setStatusTip('Removes Duplicate') ####
        btn7 = QPushButton('Upload',self)
        btn7.resize(75,50)
        btn7.move(20,210)
        btn7.setStatusTip('Uploads online')
        btn8 = QPushButton('Backup',self)
        btn8.resize(75,50)
        btn8.move(100,210)
        btn8.setStatusTip('Backup Contacts')
        btn9 = QPushButton('Share',self)
        btn9.resize(75,50)
        btn9.move(175,210)
        btn9.setStatusTip('Share Contact')####
        btn10 = QPushButton('SendText',self)
        btn10.resize(75,50)
        btn10.move(20,270)
        btn10.setStatusTip('Send Text')
        btn11 = QPushButton('CallContact',self)
        btn11.resize(75,50)
        btn11.move(100,270)
        btn11.setStatusTip('Call Selected Contact')
        btn12 = QPushButton('CopyContact',self)
        btn12.resize(75,50)
        btn12.move(175,270)
        btn12.setStatusTip('Copy contact')###
        btn13 = QPushButton('Quit',self)
        btn13.resize(75,50)
        btn13.move(400,500)
        btn13.setStatusTip('Quit Application')
        #Click activities on the buttons
        btn13.clicked.connect(self.closeApplication)
        btn5.clicked.connect(self.showAllContacts)
    
    def showAllContacts(self):
        print("Output to frame")
        # cur = conObj.cursor()
        # cur.execute("SELECT DISTINCT SEQ_NO, FIRST_NAME, MIDDLE_NAME, LAST_NAME FROM CONTACTS ;")
        # rows = cur.fetchall()
        # for row in rows:
        #     NAME =  concat(FIRST_NAME,MIDDLE_NAME,LAST_NAME)
        #     frame.setText(NAME)
                  

    def closeApplication(self):
        choice = QMessageBox.question(self, 'Message',
                                      "Are you sure to quit?", QMessageBox.Yes , QMessageBox.No)
        if choice == QMessageBox.Yes:
            print('See you again ...')
            sys.exit()
        else:
            pass

    #Connect database
    def connectDB(dbFile):
        conn = None
        try:
            conn =  sqlite3.connect(dbFile)
            print("Database Version: " ,sqlite3.version)        
            print("Connecton Successful")
            return conn
            
        except Error as e:
            print(e)
        # finally:
        #     if conn:
    #         conn.close() 

    def style_Choise(self,text):
            self.styleChoise.setText(text)
            QApplication.setStyle(QStyleFactory.create(text))

#Close connection 
def closeConnect(conn):
    if conn:
        conn.close()
        print("Database connection closed")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    #Close Database Connection
    # closeConnect(conObj)
   

if __name__ == "__main__":
    main()