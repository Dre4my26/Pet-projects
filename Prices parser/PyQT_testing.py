from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUI(self):
        self.setWindowTitle("Hello, World!") # window header