from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RelativeQGridLayout(QGridLayout):

    def __init__(self, parent=None):
        super(RelativeQGridLayout, self).__init__(parent)
        self.x = 0
        self.y = 0
        self.holdX = False
        self.holdY = False

    def addLayout(self, layout, y: int, x: int, ySpan: int, xSpan: int):
        super().addLayout(layout, self.y + y, self.x + x, ySpan, xSpan)
        if self.holdX:
            self.x += x
        else:
            self.x += x + xSpan - 1
        if self.holdY:
            self.y += y
        else:
            self.y += y + ySpan - 1
    
    def addWidget(self, widget, y: int, x: int, ySpan: int, xSpan: int):
        super().addWidget(widget, self.y + y, self.x + x, ySpan, xSpan)
        if self.holdX:
            self.x += x
        else:
            self.x += x + xSpan - 1
        if self.holdY:
            self.y += y
        else:
            self.y += y + ySpan - 1

    def addItem(self, item, y: int, x: int, ySpan: int, xSpan: int):
        super().addItem(item, self.y + y, self.x + x, ySpan, xSpan)
        if self.holdX:
            self.x += x
        else:
            self.x += x + xSpan - 1
        if self.holdY:
            self.y += y
        else:
            self.y += y + ySpan - 1

def foo():
    pass



class _createDisplay:
    
    def __init__(self, main_window):
        self.gridLayout = RelativeQGridLayout()
        main_window.dropdowns = []
        main_window.checkboxes = []
        self.addDropdown(main_window=main_window, items=["A","B","C"], label='Dropdown One', fn= lambda: self.dropdownAFn(main_window))
        main_window.dropdownAFnFlag = False
        self.addDropdown(main_window=main_window, items=["D","E","F"], label='Dropdown Two', fn= lambda: self.dropdownBFn(main_window))
        self.addDropdown(main_window=main_window, items=["D","E","F"], label='Dropdown Three')
        self.gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum), self.gridLayout.y, self.gridLayout.x, 1, 1)
        self.addCheckboxes(main_window=main_window, labels=["X","Y","Z"])
        self.gridLayout.y += 1
        self.addButton(main_window=main_window, label='Generate', fn = lambda: self.generateButtonFn(main_window))

        main_window.generalLayout.addLayout(self.gridLayout)
        
    def dropdownAFn(self, main_window):
        print("dropdownAFn")
        dropdownA = main_window.dropdowns[0]
        dropdownB = main_window.dropdowns[1]
        main_window.dropdownAFnFlag = True
        dropdownB.clear()
        currentText = dropdownA.currentText()
        if currentText=="A":
            dropdownB.addItem("D")
            dropdownB.addItem("E")
            dropdownB.addItem("F")
        elif currentText=="B":
            dropdownB.addItem("1")
            dropdownB.addItem("2")
            dropdownB.addItem("3")
        else:
            pass
        main_window.dropdownAFnFlag = False

    def dropdownBFn(self, main_window):
        if not main_window.dropdownAFnFlag:
            dropdownB = main_window.dropdowns[1]
            dropdownC = main_window.dropdowns[2]
            dropdownC.clear()
            currentText = dropdownB.currentText()
            if currentText=="D":
                dropdownC.addItem("D")
                dropdownC.addItem("E")
                dropdownC.addItem("F")
            elif currentText=="E":
                dropdownC.addItem("1")
                dropdownC.addItem("2")
                dropdownC.addItem("3")
            else:
                pass

    def generateButtonFn(self, main_window):
        for dropdown in main_window.dropdowns:
            print(dropdown.currentText())

    def checkboxFn(self, main_window):
        print("Hello")

    def addDropdown(self, main_window: QMainWindow, items: list, label: str='Some dropdown', fn=foo):
        dropdownLayout = QHBoxLayout()
        dropdownLayout.addWidget(QLabel(label))
        dropdown = QComboBox()
        for item in items:
            dropdown.addItem(item)
        dropdown.currentTextChanged.connect(fn)
        main_window.dropdowns.append(dropdown)
        dropdownLayout.addWidget(dropdown)
        self.gridLayout.addLayout(dropdownLayout,self.gridLayout.y,self.gridLayout.x,1,2)

    def addButton(self, main_window: QMainWindow, label: str='Some button', fn=foo):
        button = QPushButton(label, main_window)
        button.clicked.connect(fn)
        self.gridLayout.addWidget(button, self.gridLayout.y, self.gridLayout.x, 1, 1)


    def addCheckboxes(self, main_window: QMainWindow, labels: list, fn=foo):
        checkboxLayout = QVBoxLayout()
        for label in labels:
            checkbox = QCheckBox(label)
            checkbox.stateChanged.connect(fn)
            checkboxLayout.addWidget(checkbox)
            main_window.checkboxes.append(checkbox)
        self.gridLayout.addLayout(checkboxLayout,self.gridLayout.y,self.gridLayout.x,len(labels),1)


