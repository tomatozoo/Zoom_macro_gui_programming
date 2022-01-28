from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import time

class MyFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(5,5,self)
        self.table.setHorizontalHeaderLabels(["", "종목명", "현재가(문자)", "현재가(숫자)", "거래량"])
