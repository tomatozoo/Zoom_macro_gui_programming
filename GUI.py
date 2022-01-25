import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ZOOM 알림 프로그램')
        
        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)  
        
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
   
# Qt Designer 설치 화면
# https://azsxdcfv.tistory.com/1
#https://jy-tblog.tistory.com/26
# https://velog.io/@wlxo0401/PyQt-02-Python-GUI-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-PyQt-UI-%EC%83%9D%EC%84%B1-%EB%B0%8F-%EC%97%B0%EA%B2%B0

# PyQt 튜토리얼
# https://wikidocs.net/21860