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
        self.hour = QComboBox(self)
        self.hour.setFont(QFont('맑은 고딕',15))
        self.hour.addItem('1')
        self.hour.addItem('2')
        self.hour.addItem('3')
        self.hour.addItem('4')
        self.hour.addItem('5')
        self.hour.addItem('6')
        self.hour.addItem('7')
        self.hour.addItem('8')
        self.hour.addItem('9')
        self.hour.addItem('10')
        self.hour.addItem('11')
        self.hour.addItem('12')
        self.hour.move(50, 50)

        grid.addWidget(self.hour, 2,1)            

         # 분 선택하기
        self.min = QComboBox(self)
        self.min.setFont(QFont('맑은 고딕',15))
        self.min.addItem('0')
        self.min.addItem('1')
        self.min.addItem('2')
        self.min.addItem('3')
        self.min.addItem('4')
        self.min.addItem('5')
        self.min.addItem('6')
        self.min.addItem('7')
        self.min.addItem('8')
        self.min.addItem('9')
        self.min.addItem('10')
        self.min.addItem('11')
        self.min.addItem('12')
        self.min.addItem('13')
        self.min.addItem('14')
        self.min.addItem('15')
        self.min.addItem('16')
        self.min.addItem('17')
        self.min.addItem('18')
        self.min.addItem('19')
        self.min.addItem('20')
        self.min.addItem('21')
        self.min.addItem('22')
        self.min.addItem('23')
        self.min.addItem('24')
        self.min.addItem('25')
        self.min.addItem('26')
        self.min.addItem('27')
        self.min.addItem('28')
        self.min.addItem('29')
        self.min.addItem('30')
        self.min.addItem('31')
        self.min.addItem('32')
        self.min.addItem('33')
        self.min.addItem('34')
        self.min.addItem('35')
        self.min.addItem('36')
        self.min.addItem('37')
        self.min.addItem('38')
        self.min.addItem('39')
        self.min.addItem('40')
        self.min.addItem('41')
        self.min.addItem('42')
        self.min.addItem('43')
        self.min.addItem('44')
        self.min.addItem('45')
        self.min.addItem('46')
        self.min.addItem('47')
        self.min.addItem('48')
        self.min.addItem('49')
        self.min.addItem('50')
        self.min.addItem('51')
        self.min.addItem('52')
        self.min.addItem('53')
        self.min.addItem('54')
        self.min.addItem('55')
        self.min.addItem('56')
        self.min.addItem('57')
        self.min.addItem('58')
        self.min.addItem('59')
        self.min.move(50, 50)

        grid.addWidget(self.min, 2,2)    
        
               
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
        self.subjectName_input.setFixedWidth(300)
        self.subjectName_input.setFont(QFont('맑은 고딕',20))
        self.zoomID_input = QLineEdit()
        self.zoomID_input.setFont(QFont('맑은 고딕',20))        
        self.zoomPW_input = QLineEdit()
        self.zoomPW_input.setFont(QFont('맑은 고딕',20))
        self.subjectName_input.setMaxLength(10)
        self.zoomID_input.setMaxLength(15)
        self.zoomPW_input.setMaxLength(15)
                
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
        # 데이터를 수집합니다. 
        day_data = self.clicked_days[0].text() # 요일
        
        time_data = self.clicked_times[0].text() # 오전 오후
        hour_data = int(self.hour.currentText())
        min_data = int(self.min.currentText())
        if time_data == 'AM':
            total_time_data = str(f'{hour_data}:{min_data}')
        else:
            total_time_data = str(f'{hour_data+12}:{min_data}')
        
        sound_data = self.clicked_sounds[0].text() # 소리 유무
        if sound_data == 'On':
            sound_data = 1 # on은 1
        else:
            sound_data = 0 # off는 0
        
        subject_data = self.subjectName_input.text() 
        id_data = int(self.zoomID_input.text())
        pw_data = int(self.zoomPW_input.text())

        print(day_data, total_time_data, subject_data, id_data, pw_data, sound_data)
        
        cursor.execute("INSERT INTO alarm VALUES (?, ?, ?, ?, ?, ?)", (day_data, total_time_data, subject_data, id_data, pw_data, sound_data) )
        cursor.fetchall()
        print("select all \n\n\n\n\n")
        cursor.execute("SELECT * FROM alarm")
        con.commit()
        
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
        self.dbTable.setRowCount(4)
        self.dbTable.setColumnCount(6)
        self.dbTable.setHorizontalHeaderLabels(["요일", "알람 시간", "과목 이름", "줌 회의 아이디", "줌 회의 비밀번호", "알람 소리 여부"])
        self.setTableWidgetData()
        
        #grid.addWidget(QLabel('SQL DB가 올 자리입니다 :)'), 1,0)
        grid.addWidget(self.dbTable, 2,0)

        vbox = QWidget(self)
        self.setCentralWidget(vbox)
        vbox.setLayout(grid)

        self.resize(600, 800)
        self.show()    
    
    def setTableWidgetData(self):
        cursor.execute("SELECT * FROM alarm")
        
        
        output = cursor.fetchone()
        print(output)
        self.dbTable.setFont(QFont('맑은 고딕',10))
        self.dbTable.setItem(0,0,QTableWidgetItem(output[0]))
        
        self.dbTable.setItem(0,1,QTableWidgetItem(output[1]))
        self.dbTable.setItem(0,2,QTableWidgetItem(output[2]))
        self.dbTable.setItem(0,3,QTableWidgetItem(str(output[3])))
        self.dbTable.setItem(0,4,QTableWidgetItem(str(output[4])))
        self.dbTable.setItem(0,5,QTableWidgetItem(str(output[5])))
       
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
