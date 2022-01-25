# 모듈을 불러옵니다. 
import sys
from PyQt5.QtWidgets import qApp, QAction, QGridLayout, QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon, QFont
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
        grid = QGridLayout()
        self.setLayout(grid)
        
        grid.addWidget(QLabel('Create New'), 0,0)
        grid.addWidget(QLineEdit(), 0,1)
        
        # 메뉴바를 만드는 코드입니다. 
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # 상태바를 만드는 코드입니다. 
        self.statusBar().showMessage('Ready')
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        
        # 툴바를 만드는 코드입니다. 
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        # 메뉴를 만드는 코드입니다. 
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # 툴팁을 만드는 코드입니다. 
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        # 화면의 아이콘과 이미지를 설정해주는 코드입니다. 
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ZOOM 알림 프로그램')
        
        # 버튼입니다. 
        btn = QPushButton('버튼입니다', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)  
        
        # 위젯 라벨을 만들어줍니다. 
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')
        
        # 각 위젯에 스타일을 적용해줍니다. 
        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QWidget(self)
        self.setCentralWidget(vbox)
        
        layout = QVBoxLayout()
        layout.addWidget(lbl_red)
        layout.addWidget(lbl_green)
        layout.addWidget(lbl_blue)


        vbox.setLayout(layout)
        
        # 화면 구성 요소를 설정해줍니다. 
        self.move(300, 300)
        self.resize(600, 800)
        self.center()
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