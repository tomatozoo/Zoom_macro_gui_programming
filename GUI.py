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
        self.initSETTING()

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

    def initSETTING(self):
        self.clicked_days = []
        self.clicked_times = []
        self.clicked_sounds = []
    
    def connect_days(self, someday):
        for i in self.clicked_days:
            if i == someday:
                self.clicked_days.remove(i)
                return
            i.toggle()
            self.clicked_days.remove(i)
        self.clicked_days.append(someday)
    def connect_times(self, someday):
        for i in self.clicked_times:
            if i == someday:
                self.clicked_times.remove(i)
                return
            i.toggle()
            self.clicked_times.remove(i)
        self.clicked_times.append(someday)
    def connect_sounds(self, someday):
        for i in self.clicked_sounds:
            if i == someday:
                self.clicked_sounds.remove(i)
                return
            i.toggle()
            self.clicked_sounds.remove(i)
        self.clicked_sounds.append(someday)       
    def btn1_clicked(self):
        # 그리드 레이아웃으로 화면을 구성합니다. 
        grid = QGridLayout()
        self.setLayout(grid)

        # 월요일 버튼
        self.monday = QPushButton('Mon', self)
        self.monday.setFont(QFont('맑은 고딕',20))
        self.monday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.monday.setMaximumHeight(30)
        self.monday.setCheckable(True)
        self.monday.clicked.connect(lambda : self.connect_days(self.monday))
        grid.addWidget(self.monday, 0,0)

        # 화요일 버튼
        self.tuesday = QPushButton('Tue', self)
        self.tuesday.setFont(QFont('맑은 고딕',20))
        self.tuesday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.tuesday.setMaximumHeight(30)
        self.tuesday.setCheckable(True)
        self.tuesday.clicked.connect(lambda : self.connect_days(self.tuesday))
        grid.addWidget(self.tuesday, 0,1)
        
        # 수요일 버튼
        self.wednesday = QPushButton('Wed', self)
        self.wednesday.setFont(QFont('맑은 고딕',20))
        self.wednesday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.wednesday.setMaximumHeight(30)
        self.wednesday.setCheckable(True)
        self.wednesday.clicked.connect(lambda : self.connect_days(self.wednesday))
        grid.addWidget(self.wednesday, 0,2)
        
        # 목요일 버튼
        self.thursday = QPushButton('Thu', self)
        self.thursday.setFont(QFont('맑은 고딕',20))
        self.thursday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.thursday.setMaximumHeight(30)
        self.thursday.setCheckable(True)
        self.thursday.clicked.connect(lambda : self.connect_days(self.thursday))
        grid.addWidget(self.thursday, 0,3)

        # 금요일 버튼
        self.friday = QPushButton('Fri', self)
        self.friday.setFont(QFont('맑은 고딕',20))
        self.friday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.friday.setMaximumHeight(30)
        self.friday.setCheckable(True)
        self.friday.clicked.connect(lambda : self.connect_days(self.friday))
        grid.addWidget(self.friday, 0,4)

        # 토요일 버튼
        self.saturday = QPushButton('Sat', self)
        self.saturday.setFont(QFont('맑은 고딕',20))
        self.saturday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.saturday.setMaximumHeight(30)
        self.saturday.setCheckable(True)
        self.saturday.clicked.connect(lambda : self.connect_days(self.saturday))
        grid.addWidget(self.saturday, 0,5)
        
        # 일요일 버튼
        self.sunday = QPushButton('Sun', self)
        self.sunday.setFont(QFont('맑은 고딕',20))
        self.sunday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.sunday.setMaximumHeight(30)
        self.sunday.setCheckable(True)
        self.sunday.clicked.connect(lambda : self.connect_days(self.sunday))
        grid.addWidget(self.sunday, 0,6)
        
        # AM 버튼
        self.am = QPushButton('AM', self)
        self.am.setFont(QFont('맑은 고딕',20))
        self.am.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.am.setMaximumHeight(30)
        self.am.setCheckable(True)
        self.am.clicked.connect(lambda : self.connect_times(self.am))

        grid.addWidget(self.am, 1,0)
        
        # PM 버튼
        self.pm = QPushButton('PM', self)
        self.pm.setFont(QFont('맑은 고딕',20))
        self.pm.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.pm.setMaximumHeight(30)
        self.pm.setCheckable(True)
        self.pm.clicked.connect(lambda : self.connect_times(self.pm))

        grid.addWidget(self.pm, 3,0)      
                
        
        # 시간 / 분 선택하기
        cb = QComboBox(self)
        cb.setFont(QFont('맑은 고딕',15))
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
        cb.setFont(QFont('맑은 고딕',15))
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
        subjectName = QLabel('Subject Name :')
        subjectName.setFont(QFont('맑은 고딕',20))
        grid.addWidget(subjectName, 4, 0)
        zoomID = QLabel('Zoom PMI :')
        zoomID.setFont(QFont('맑은 고딕',20))
        grid.addWidget(zoomID, 5, 0)
        zoomPW = QLabel('Zoom Password :')
        zoomPW.setFont(QFont('맑은 고딕',20))
        grid.addWidget(zoomPW, 6, 0)
        
        self.subjectName_input = QLineEdit()
        self.subjectName_input.setFont(QFont('맑은 고딕',20))
        self.zoomID_input = QLineEdit()
        self.zoomID_input.setFont(QFont('맑은 고딕',20))        
        self.zoomPW_input = QLineEdit()
        self.zoomPW_input.setFont(QFont('맑은 고딕',20))
                
        grid.addWidget(self.subjectName_input, 4, 1)
        grid.addWidget(self.zoomID_input, 5, 1)
        grid.addWidget(self.zoomPW_input, 6, 1)

        sound = QLabel('Sound :')
        sound.setFont(QFont('맑은 고딕',20))
        grid.addWidget(sound, 7, 0)
        
        self.sound_on = QPushButton('On', self)
        self.sound_on.setFont(QFont('맑은 고딕',20))
        self.sound_on.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.sound_on.setMaximumHeight(30)
        self.sound_on.setCheckable(True)
        self.sound_on.clicked.connect(lambda : self.connect_sounds(self.sound_on))

        grid.addWidget(self.sound_on, 7,1)

        self.sound_off = QPushButton('Off', self)
        self.sound_off.setFont(QFont('맑은 고딕',20))
        self.sound_off.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
        self.sound_off.setMaximumHeight(30)
        self.sound_off.setCheckable(True)
        self.sound_off.clicked.connect(lambda : self.connect_sounds(self.sound_off))

        grid.addWidget(self.sound_off, 7,2)

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
