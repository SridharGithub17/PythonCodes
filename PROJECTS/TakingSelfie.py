#!/bin/usr/python
from pyqtgraph import ImageView

class StartWindow(QMainWindow):
    def __init__(self, camera = None):
        [...]
        self.image_view = ImageView()
        self.layout.addWidget(self.image_view)


def main():
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()