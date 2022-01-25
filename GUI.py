# 모듈을 불러옵니다. 
import sys
from PyQt5.QtWidgets import *
#qApp, QAction, QGridLayout, QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import *
#QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt


# 메인 클래스를 계획합니다. 
class MyApp(QMainWindow, QWidget):
    # UI 화면을 초기화해줍니다. 
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate() # 오늘 날짜를 받아옵니다. 
        self.initUI()

    # UI에 포함될 구성요소의 기본적인 설정을 수행해줍니다. 
    def initUI(self):
        # 화면의 아이콘과 이미지를 설정해주는 코드입니다. 
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.setWindowTitle('ZOOM 알림 프로그램')   
        # 화면의 배경색상을 흰색으로 설정해줍니다. 
        pal = QPalette()  
        pal.setColor(QPalette.Background,QColor(255,255,255))
        self.setAutoFillBackground(True)
        self.setPalette(pal)   
        
        # 그리드 레이아웃으로 화면을 구성합니다. 
        grid = QGridLayout()
        self.setLayout(grid)

        # 첫 화면에 두기 위한 버튼을 생성합니다. 
        btn1 = QPushButton('Create New', self)
        btn1.setFont(QFont('Times',20))
        btn1.setStyleSheet('QPushButton {background-color: deepskyblue;color:white;}')
        btn1.setMaximumHeight(100)
        btn1.setCheckable(False)
        btn1.toggle()

        grid.addWidget(btn1, 0,0)
        grid.addWidget(QLabel(), 1,0)

        vbox = QWidget(self)
        self.setCentralWidget(vbox)
        vbox.setLayout(grid)

        self.resize(600, 800)
        self.show()

    def center(self):
        # GUI 프로그램을 화면의 정가운데 띄웁니다. 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# 메인에서 실행해줍니다. 
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