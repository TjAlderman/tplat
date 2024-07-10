import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui import _createDisplay

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle("PyQt Demo App")
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self.centralWidget)

        _createDisplay(self)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()