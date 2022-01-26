# 모듈을 불러옵니다. 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, QDate, Qt
from PyQt5 import QtSql


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
        self.setWindowIcon(QIcon('./images/web.png'))
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
        btn1.setFont(QFont('맑은 고딕',20))
        btn1.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        btn1.setMaximumHeight(100)
        btn1.setCheckable(False)
        btn1.toggle()
        btn1.clicked.connect(self.btn1_clicked)

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

    def btn1_clicked(self):
        # 그리드 레이아웃으로 화면을 구성합니다. 
        grid = QGridLayout()
        self.setLayout(grid)

        # 월요일 버튼
        monday = QPushButton('Mon', self)
        monday.setFont(QFont('맑은 고딕',20))
        monday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        monday.setMaximumHeight(30)
        monday.setCheckable(True)
        monday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(monday, 0,0)

        # 화요일 버튼
        tuesday = QPushButton('Tue', self)
        tuesday.setFont(QFont('맑은 고딕',20))
        tuesday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        tuesday.setMaximumHeight(30)
        tuesday.setCheckable(False)
        tuesday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(tuesday, 0,1)
        
        # 수요일 버튼
        wednesday = QPushButton('Wed', self)
        wednesday.setFont(QFont('맑은 고딕',20))
        wednesday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        wednesday.setMaximumHeight(30)
        wednesday.setCheckable(False)
        wednesday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(wednesday, 0,2)
        
        # 목요일 버튼
        thursday = QPushButton('Thu', self)
        thursday.setFont(QFont('맑은 고딕',20))
        thursday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        thursday.setMaximumHeight(30)
        thursday.setCheckable(False)
        thursday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(thursday, 0,3)

        # 금요일 버튼
        friday = QPushButton('Fri', self)
        friday.setFont(QFont('맑은 고딕',20))
        friday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        friday.setMaximumHeight(30)
        friday.setCheckable(False)
        friday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(friday, 0,4)

        # 토요일 버튼
        saturday = QPushButton('Sat', self)
        saturday.setFont(QFont('맑은 고딕',20))
        saturday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        saturday.setMaximumHeight(30)
        saturday.setCheckable(False)
        saturday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(saturday, 0,5)
        
        # 일요일 버튼
        sunday = QPushButton('Sun', self)
        sunday.setFont(QFont('맑은 고딕',20))
        sunday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        sunday.setMaximumHeight(30)
        sunday.setCheckable(False)
        sunday.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(sunday, 0,6)
        
        # AM 버튼
        am = QPushButton('AM', self)
        am.setFont(QFont('맑은 고딕',20))
        am.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        am.setMaximumHeight(30)
        am.setCheckable(False)
        am.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(am, 1,0)
        
        # PM 버튼
        pm = QPushButton('PM', self)
        pm.setFont(QFont('맑은 고딕',20))
        pm.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        pm.setMaximumHeight(30)
        pm.setCheckable(False)
        pm.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(pm, 3,0)      
                
        
        # 시간 / 분 선택하기
        cb = QComboBox(self)
        cb.addItem('1')
        cb.addItem('2')
        cb.addItem('3')
        cb.addItem('4')
        cb.addItem('5')
        cb.addItem('6')
        cb.addItem('7')
        cb.addItem('8')
        cb.addItem('9')
        cb.addItem('10')
        cb.addItem('11')
        cb.addItem('12')
        cb.move(50, 50)

        grid.addWidget(cb, 2,1)            

         # 분 선택하기
        cb = QComboBox(self)
        cb.addItem('0')
        cb.addItem('1')
        cb.addItem('2')
        cb.addItem('3')
        cb.addItem('4')
        cb.addItem('5')
        cb.addItem('6')
        cb.addItem('7')
        cb.addItem('8')
        cb.addItem('9')
        cb.addItem('10')
        cb.addItem('11')
        cb.addItem('12')
        cb.addItem('13')
        cb.addItem('14')
        cb.addItem('15')
        cb.addItem('16')
        cb.addItem('17')
        cb.addItem('18')
        cb.addItem('19')
        cb.addItem('20')
        cb.addItem('21')
        cb.addItem('22')
        cb.addItem('23')
        cb.addItem('24')
        cb.addItem('25')
        cb.addItem('26')
        cb.addItem('27')
        cb.addItem('28')
        cb.addItem('29')
        cb.addItem('30')
        cb.addItem('31')
        cb.addItem('32')
        cb.addItem('33')
        cb.addItem('34')
        cb.addItem('35')
        cb.addItem('36')
        cb.addItem('37')
        cb.addItem('38')
        cb.addItem('39')
        cb.addItem('40')
        cb.addItem('41')
        cb.addItem('42')
        cb.addItem('43')
        cb.addItem('44')
        cb.addItem('45')
        cb.addItem('46')
        cb.addItem('47')
        cb.addItem('48')
        cb.addItem('49')
        cb.addItem('50')
        cb.addItem('51')
        cb.addItem('52')
        cb.addItem('53')
        cb.addItem('54')
        cb.addItem('55')
        cb.addItem('56')
        cb.addItem('57')
        cb.addItem('58')
        cb.addItem('59')
        cb.move(50, 50)

        grid.addWidget(cb, 2,2)    
        
               
        # 교과목 설정하기
        grid.addWidget(QLabel('Subject Name :'), 4, 0)
        grid.addWidget(QLabel('Zoom PMI :'), 5, 0)
        grid.addWidget(QLabel('Zoom Password :'), 6, 0)

        grid.addWidget(QLineEdit(), 4, 1)
        grid.addWidget(QLineEdit(), 5, 1)
        grid.addWidget(QLineEdit(), 6, 1)

        grid.addWidget(QLabel('Sound :'), 7, 0)
        
        sound_on = QPushButton('On', self)
        sound_on.setFont(QFont('맑은 고딕',20))
        sound_on.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        sound_on.setMaximumHeight(30)
        sound_on.setCheckable(False)
        sound_on.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(sound_on, 7,1)

        sound_off = QPushButton('Off', self)
        sound_off.setFont(QFont('맑은 고딕',20))
        sound_off.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        sound_off.setMaximumHeight(30)
        sound_off.setCheckable(False)
        sound_off.toggle()
        #sound_on.clicked.connect(self.btn1_clicked)

        grid.addWidget(sound_off, 7,2)

        OK = QPushButton('OK', self)
        OK.setFont(QFont('맑은 고딕',20))
        OK.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        OK.setMaximumHeight(30)
        OK.setCheckable(False)
        OK.toggle()
        OK.clicked.connect(self.OK_clicked)

        grid.addWidget(OK, 8,0)
        
        cancel = QPushButton('Cancel', self)
        cancel.setFont(QFont('맑은 고딕',20))
        cancel.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        cancel.setMaximumHeight(30)
        cancel.setCheckable(False)
        cancel.toggle()
        cancel.clicked.connect(self.cancel_clicked)

        grid.addWidget(cancel, 8,1)
                        
        vbox = QWidget(self)
        self.setCentralWidget(vbox)
        vbox.setLayout(grid)

        self.resize(600, 800)
        self.show()    

    def OK_clicked(self):
        # 그리드 레이아웃으로 화면을 구성합니다. 
        grid = QGridLayout()
        self.setLayout(grid)

        # 첫 화면에 두기 위한 버튼을 생성합니다. 
        btn1 = QPushButton('Create New', self)
        btn1.setFont(QFont('맑은 고딕',20))
        btn1.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        btn1.setMaximumHeight(100)
        btn1.setCheckable(False)
        btn1.toggle()
        btn1.clicked.connect(self.btn1_clicked)

        grid.addWidget(btn1, 0,0)
        
        self.dbTable = QTableWidget(self)
        self.dbTable.resize(290,290)
        self.dbTable.setRowCount(2)
        self.dbTable.setColumnCount(2)
        self.setTableWidgetData()
        
        grid.addWidget(QLabel('SQL DB가 올 자리입니다 :)'), 1,0)
        grid.addWidget(self.dbTable, 2,0)

        vbox = QWidget(self)
        self.setCentralWidget(vbox)
        vbox.setLayout(grid)

        self.resize(600, 800)
        self.show()    
    
    def setTableWidgetData(self):
        self.dbTable.setItem(0,0,QTableWidgetItem("(0,0)"))
        self.dbTable.setItem(0,1,QTableWidgetItem("(0,0)"))
        self.dbTable.setItem(1,0,QTableWidgetItem("(0,0)"))
        self.dbTable.setItem(1,1,QTableWidgetItem("(0,0)"))
        
    def cancel_clicked(self):
        self.initUI()
        
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

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