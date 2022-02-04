# 모듈을 불러옵니다. 
import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSql, uic
from PyQt5.QtMultimedia import QSound
import os
import time
import threading
import datetime
import json
import webbrowser

class DB():
    def __init__(self):
        # DB를 생성한다. 
        self.con = sqlite3.connect('simpledb.sqlite')
        # 데이터 삽입
        # connection 객체인 con을 이용해서 cursor 객체를 생성함
        self.cursor = self.con.cursor()
        
        try:
            self.cursor.execute("CREATE table zoomlist (DAYLIST TEXT, HOURMIN TEXT, SUBJECTNAME TEXT, ZOOMID INTEGER, ZOOMPW TEXT, SOUND INTEGER)")
        except:
            # 그러지 않아도 되는 경우
            pass   
        self.line = 0     
    def create(self, row_list):
        self.cursor.execute("INSERT INTO zoomlist VALUES (?, ?, ?, ?, ?, ?)", row_list)
        self.con.commit()
    def read(self):
        for row in self.cursor.execute('SELECT * FROM zoomlist ORDER BY SOUND'):
            print(row)
        self.con.commit()
    def update(self):
        self.line = 0
        for row in self.cursor.execute('SELECT * FROM zoomlist ORDER BY SOUND'):
            self.line += 1
        self.con.commit()
    def delete(self, where):
        self.cursor.execute("DELETE FROM zoomlist WHERE HOURMIN = ? AND SUBJECTNAME = ? AND ZOOMID = ? AND ZOOMPW = ? AND SOUND = ?", where)
        self.con.commit()
  
# 메인 클래스를 계획합니다. 
class MyApp(QMainWindow, QWidget):
    # UI 화면을 초기화해줍니다. 
    def __init__(self):
        try:
            super().__init__()
            self.date = QDate.currentDate() # 오늘 날짜를 받아옵니다. 
            self.db = DB()
            self.initUI()
            self.db.read()
            self.db.update()
            self.initSETTING()
            
            self.timer = QTimer(self)
            self.timer.start(1000)
            self.timer.timeout.connect(self.check_alarm)
            self.true = True
            self.current = True
            self.next_alarm_time = 0
            
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass        
        
    # UI에 포함될 구성요소의 기본적인 설정을 수행해줍니다. 
    def initUI(self):
        try:
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
            
            dele = QPushButton('Delete rows', self)
            dele.setFont(QFont('맑은 고딕',20))
            dele.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            dele.setMaximumHeight(100)
            dele.setCheckable(False)
            dele.toggle()
            dele.clicked.connect(self.delete_one)

            grid.addWidget(dele, 1,0)

            self.dbTable = QTableWidget(self)
            self.db.update()
            self.dbTable.setRowCount(self.db.line)
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
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def center(self):
        try:
            # GUI 프로그램을 화면의 정가운데 띄웁니다. 
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def initSETTING(self):
        try:
            self.clicked_days = []
            self.clicked_times = []
            self.clicked_sounds = []
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def connect_days(self, someday):
        try:
            for i in self.clicked_days:
                if i == someday:
                    self.clicked_days.remove(i)
                    return
                i.toggle()
                self.clicked_days.remove(i)
            self.clicked_days.append(someday)
        except:
            msg = QMessageBox()
    def connect_times(self, someday):
        try:
            for i in self.clicked_times:
                if i == someday:
                    self.clicked_times.remove(i)
                    return
                i.toggle()
                self.clicked_times.remove(i)
            self.clicked_times.append(someday)
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def connect_sounds(self, someday):
        try:
            for i in self.clicked_sounds:
                if i == someday:
                    self.clicked_sounds.remove(i)
                    return
                i.toggle()
                self.clicked_sounds.remove(i)
            self.clicked_sounds.append(someday)       
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def btn1_clicked(self):
        try:
            # 그리드 레이아웃으로 화면을 구성합니다. 
            # 메인 그리드 레이아웃
            grid = QGridLayout()
            self.setLayout(grid)

            sub_grid1 = QGridLayout()
            # 월요일 버튼
            self.monday = QPushButton('Mon', self)
            self.monday.setFont(QFont('맑은 고딕',20))
            self.monday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.monday.setMaximumHeight(30)
            self.monday.setCheckable(True)
            self.monday.clicked.connect(lambda : self.connect_days(self.monday))
            sub_grid1.addWidget(self.monday, 0,0)

            # 화요일 버튼
            self.tuesday = QPushButton('Tue', self)
            self.tuesday.setFont(QFont('맑은 고딕',20))
            self.tuesday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.tuesday.setMaximumHeight(30)
            self.tuesday.setCheckable(True)
            self.tuesday.clicked.connect(lambda : self.connect_days(self.tuesday))
            sub_grid1.addWidget(self.tuesday, 0,1)
            
            # 수요일 버튼
            self.wednesday = QPushButton('Wed', self)
            self.wednesday.setFont(QFont('맑은 고딕',20))
            self.wednesday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.wednesday.setMaximumHeight(30)
            self.wednesday.setCheckable(True)
            self.wednesday.clicked.connect(lambda : self.connect_days(self.wednesday))
            sub_grid1.addWidget(self.wednesday, 0,2)
            
            # 목요일 버튼
            self.thursday = QPushButton('Thu', self)
            self.thursday.setFont(QFont('맑은 고딕',20))
            self.thursday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.thursday.setMaximumHeight(30)
            self.thursday.setCheckable(True)
            self.thursday.clicked.connect(lambda : self.connect_days(self.thursday))
            sub_grid1.addWidget(self.thursday, 0,3)

            # 금요일 버튼
            self.friday = QPushButton('Fri', self)
            self.friday.setFont(QFont('맑은 고딕',20))
            self.friday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.friday.setMaximumHeight(30)
            self.friday.setCheckable(True)
            self.friday.clicked.connect(lambda : self.connect_days(self.friday))
            sub_grid1.addWidget(self.friday, 0,4)

            # 토요일 버튼
            self.saturday = QPushButton('Sat', self)
            self.saturday.setFont(QFont('맑은 고딕',20))
            self.saturday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.saturday.setMaximumHeight(30)
            self.saturday.setCheckable(True)
            self.saturday.clicked.connect(lambda : self.connect_days(self.saturday))
            sub_grid1.addWidget(self.saturday, 0,5)
            
            # 일요일 버튼
            self.sunday = QPushButton('Sun', self)
            self.sunday.setFont(QFont('맑은 고딕',20))
            self.sunday.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.sunday.setMaximumHeight(30)
            self.sunday.setCheckable(True)
            self.sunday.clicked.connect(lambda : self.connect_days(self.sunday))
            sub_grid1.addWidget(self.sunday, 0,6)
            
            
            grid.addLayout(sub_grid1, 0,0)
            
            sub_grid2 = QGridLayout()
            # AM 버튼
            self.am = QPushButton('AM', self)
            self.am.setFont(QFont('맑은 고딕',20))
            self.am.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.am.setMaximumHeight(30)
            self.am.setCheckable(True)
            self.am.clicked.connect(lambda : self.connect_times(self.am))

            sub_grid2.addWidget(self.am, 0,0)
            
            # PM 버튼
            self.pm = QPushButton('PM', self)
            self.pm.setFont(QFont('맑은 고딕',20))
            self.pm.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.pm.setMaximumHeight(30)
            self.pm.setCheckable(True)
            self.pm.clicked.connect(lambda : self.connect_times(self.pm))

            sub_grid2.addWidget(self.pm, 0,1)      
                    
            
            # 시간 / 분 선택하기
            hour_label = QLabel('시간 : ')
            hour_label.setFont(QFont('맑은 고딕',20))
            
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

            sub_grid2.addWidget(self.hour, 1,0)            

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

            sub_grid2.addWidget(self.min, 1,1)
            
            min_label = QLabel('분 : ')
            min_label.setFont(QFont('맑은 고딕',20))
                        

            
            grid.addLayout(sub_grid2, 1,0)
            
            sub_grid3 = QGridLayout()        
                
            # 교과목 설정하기
            subjectName = QLabel('Subject Name :')
            subjectName.setFont(QFont('맑은 고딕',20))
            sub_grid3.addWidget(subjectName, 0, 0)
            zoomID = QLabel('Zoom PMI (숫자만):')
            zoomID.setFont(QFont('맑은 고딕',20))
            sub_grid3.addWidget(zoomID, 1, 0)
            zoomPW = QLabel('Zoom Password :')
            zoomPW.setFont(QFont('맑은 고딕',20))
            sub_grid3.addWidget(zoomPW, 2, 0)
            
            self.subjectName_input = QLineEdit()
            self.subjectName_input.setFont(QFont('맑은 고딕',20))
            self.zoomID_input = QLineEdit()
            self.zoomID_input.setFont(QFont('맑은 고딕',20))        
            self.zoomPW_input = QLineEdit()
            self.zoomPW_input.setFont(QFont('맑은 고딕',20))
            self.subjectName_input.setMaxLength(15)
            self.zoomID_input.setMaxLength(15)
            self.zoomPW_input.setMaxLength(15)
                    
            sub_grid3.addWidget(self.subjectName_input, 0, 1)
            sub_grid3.addWidget(self.zoomID_input, 1, 1)
            sub_grid3.addWidget(self.zoomPW_input, 2, 1)


            grid.addLayout(sub_grid3, 2,0)

            sub_grid4 = QGridLayout()        
            
            sound = QLabel('Sound :')
            sound.setFont(QFont('맑은 고딕',20))
            sub_grid4.addWidget(sound, 0, 0)
            
            
            self.sound_on = QPushButton('On', self)
            self.sound_on.setFont(QFont('맑은 고딕',20))
            self.sound_on.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.sound_on.setMaximumHeight(30)
            self.sound_on.setCheckable(True)
            self.sound_on.clicked.connect(lambda : self.connect_sounds(self.sound_on))

            sub_grid4.addWidget(self.sound_on, 0,1)

            self.sound_off = QPushButton('Off', self)
            self.sound_off.setFont(QFont('맑은 고딕',20))
            self.sound_off.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            self.sound_off.setMaximumHeight(30)
            self.sound_off.setCheckable(True)
            self.sound_off.clicked.connect(lambda : self.connect_sounds(self.sound_off))

            sub_grid4.addWidget(self.sound_off, 0,2)
            
            grid.addLayout(sub_grid4, 3,0)

            sub_grid5 = QGridLayout()
        
            OK = QPushButton('OK', self)
            OK.setFont(QFont('맑은 고딕',20))
            OK.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            OK.setMaximumHeight(30)
            OK.setCheckable(False)
            OK.toggle()
            OK.clicked.connect(self.OK_clicked)

            sub_grid5.addWidget(OK, 0,0)
            
            cancel = QPushButton('Cancel', self)
            cancel.setFont(QFont('맑은 고딕',20))
            cancel.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            cancel.setMaximumHeight(30)
            cancel.setCheckable(False)
            cancel.toggle()
            cancel.clicked.connect(self.cancel_clicked)

            sub_grid5.addWidget(cancel, 0,1)
            grid.addLayout(sub_grid5, 4, 0)

            vbox = QWidget(self)
            self.setCentralWidget(vbox)
            vbox.setLayout(grid)

            self.resize(600, 800)
            self.show()    
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def OK_clicked(self):
        try:
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
            pw_data = self.zoomPW_input.text()
            
            new_row = [day_data, total_time_data, subject_data, id_data, pw_data, sound_data]
            print(new_row)
            self.db.create(new_row)
            
            self.initUI()
            self.initSETTING()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('WARNING')
            msg.setText('입력 양식을 지켜주세요')
            msg.setWindowIcon(QIcon('./images/edit.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass        
    def setTableWidgetData_deletion(self):
        try:
            self.dbTable.setFont(QFont('맑은 고딕',10))
            self.checkBoxList = []
            for i in range(self.db.line):
                ckbox = QCheckBox()
                self.checkBoxList.append(ckbox)
                
            for i in range(self.db.line):
                cellWidget = QWidget()
                layoutCB = QHBoxLayout(cellWidget)
                layoutCB.addWidget(self.checkBoxList[i])
                layoutCB.setAlignment(Qt.AlignCenter)
                layoutCB.setContentsMargins(0,0,0,0)
                cellWidget.setLayout(layoutCB)
                
                self.dbTable.setCellWidget(i,0,cellWidget)
                
            i = 0
            for row in self.db.cursor.execute('SELECT * FROM zoomlist ORDER BY SOUND'):
                self.dbTable.setItem(i,1,QTableWidgetItem(f'{row[1]}'))
                self.dbTable.setItem(i,2,QTableWidgetItem(f'{row[2]}'))
                self.dbTable.setItem(i,3,QTableWidgetItem(f'{row[3]}'))
                self.dbTable.setItem(i,4,QTableWidgetItem(f'{row[4]}'))
                self.dbTable.setItem(i,5,QTableWidgetItem(f'{row[5]}'))
                
                i += 1    
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def setTableWidgetData(self):
        try:
            self.dbTable.setFont(QFont('맑은 고딕',10))
            i = 0
            for row in self.db.cursor.execute('SELECT * FROM zoomlist ORDER BY DAYLIST'):
                self.dbTable.setItem(i,0,QTableWidgetItem(f'{row[0]}'))
                self.dbTable.setItem(i,1,QTableWidgetItem(f'{row[1]}'))
                self.dbTable.setItem(i,2,QTableWidgetItem(f'{row[2]}'))
                self.dbTable.setItem(i,3,QTableWidgetItem(f'{row[3]}'))
                self.dbTable.setItem(i,4,QTableWidgetItem(f'{row[4]}'))
                self.dbTable.setItem(i,5,QTableWidgetItem(f'{row[5]}'))
                i += 1
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def cancel_clicked(self):
        try:
            self.initUI()
            self.initSETTING()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def onActivated(self, text):
        try:
            self.lbl.setText(text)
            self.lbl.adjustSize()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass            
    def delete_one(self):
        try:

            # 화면의 배경색상을 흰색으로 설정해줍니다. 
            pal = QPalette()  
            pal.setColor(QPalette.Background,QColor(255,255,255))
            self.setAutoFillBackground(True)
            self.setPalette(pal)  
            
            # 그리드 레이아웃으로 화면을 구성합니다. 
            grid = QGridLayout()
            self.setLayout(grid)

            self.dbTable = QTableWidget(self)
            self.db.update()
            self.dbTable.setRowCount(self.db.line)
            self.dbTable.setColumnCount(6)
            self.dbTable.setHorizontalHeaderLabels(["삭제 여부","요일", "알람 시간", "과목 이름", "줌 회의 아이디", "줌 회의 비밀번호", "알람 소리 여부"])
            self.setTableWidgetData_deletion()

            #grid.addWidget(QLabel('SQL DB가 올 자리입니다 :)'), 1,0)
            grid.addWidget(self.dbTable, 1,0)
            
            sub_grid5 = QGridLayout()
        
            OK = QPushButton('Delete', self)
            OK.setFont(QFont('맑은 고딕',20))
            OK.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            OK.setMaximumHeight(30)
            OK.setCheckable(False)
            OK.toggle()
            OK.clicked.connect(self.OK_clicked_delete)

            sub_grid5.addWidget(OK, 0,0)
            
            cancel = QPushButton('Cancel', self)
            cancel.setFont(QFont('맑은 고딕',20))
            cancel.setStyleSheet('QPushButton {background-color: dodgerblue;color:white;}')
            cancel.setMaximumHeight(30)
            cancel.setCheckable(False)
            cancel.toggle()
            cancel.clicked.connect(self.cancel_clicked)

            sub_grid5.addWidget(cancel, 0,1)
            grid.addLayout(sub_grid5, 2, 0)
                            
            
            vbox = QWidget(self)
            self.setCentralWidget(vbox)
            vbox.setLayout(grid)

            self.resize(600, 800)
            self.show()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass
    def OK_clicked_delete(self):
        try:
            for i in range(self.db.line):
                if self.checkBoxList[i].isChecked() == True:
                    tmp_row = []
                    for j in range(1,6):
                        tmp_row.append(self.dbTable.item(i,j).text())
                    self.db.delete(tmp_row)

            
            self.initUI()
            self.initSETTING()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setWindowIcon(QIcon('./images/web.png'))
            msg.setStandardButtons(QMessageBox.Ok)
            result = msg.exec_()
            if result == QMessageBox.Ok:
                pass
    def update_alarm(self):
            past_alarm_time = self.next_alarm_time
            dy_lis = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            xc = datetime.datetime.now()
            t = time.localtime()
            yr = str(t.tm_year) # 년
            mo = str(t.tm_mon) # 월
            if len(mo) == 1:
                mo = '0' + mo
            dt = str(t.tm_mday) # 일
            dy = dy_lis[t.tm_wday]

            # 알람 울릴 다음 시간과 줌 접속 정보를 가져온다. 
            now_time = time.strftime("%Y%m%d%H:%M", t)
            now_time = datetime.datetime.strptime(now_time, "%Y%m%d%H:%M")

            self.next_alarm_time = now_time
            past_alarm_time = now_time
            next_alarm_info = []
            for row in self.db.cursor.execute('SELECT * FROM zoomlist ORDER BY DAYLIST'):
                if dy == row[0]: # 같은 요일만 추출함
                    alarm_time = yr + mo + dt + row[1]
                    alarm_time = datetime.datetime.strptime(alarm_time, "%Y%m%d%H:%M")
                    if now_time <= alarm_time or alarm_time < self.next_alarm_time:
                        # self.true = True
                        self.next_alarm_time = alarm_time
                        self.next_alarm_info = row
                        
            if past_alarm_time != self.next_alarm_time:
                return 'change'
    def check_alarm(self):
            check = self.update_alarm() 
            if check == 'change':
                self.true = True
            # 현재 시간을 구해줍니다.
            t = time.localtime()

            now_time = time.strftime("%Y%m%d%H:%M", t)
            now_time = datetime.datetime.strptime(now_time, "%Y%m%d%H:%M")
                        
            if len(self.next_alarm_info) >= 6:
                # 접속할 수업이 있는 경우, 
                zoomid = self.next_alarm_info[3]
                zoompw = self.next_alarm_info[4]
                subject = self.next_alarm_info[2]
                sound = self.next_alarm_info[5]
                url = 'zoommtg://zoom.us/join?confno={}&pwd={}'.format(zoomid, zoompw)

                
                try:
                    min_left = str(self.next_alarm_time - now_time) # str(next_alarm_time - now_time)[-8:]
                    min_left = min_left.split(' ')[2]
                    min_left = min_left.split(':')
                    min_left = int(min_left[0]) * 60 + int(min_left[1])
                except:
                    min_left = 10
            print(now_time)
            print(min_left)
            
            while self.true:
                if 0 <= min_left <= 5:
                        webbrowser.open(url)
                        if sound == 1:
                            music = QSound('sounds/alarm.wav')
                            music.play()
                        msg = QMessageBox()
                        msg.setWindowTitle('수업 시작합니다')
                        msg.setWindowIcon(QIcon('./images/web.png'))
                        msg.setText(f'{min_left} 분 후 \n{subject} 수업이 시작됩니다')
                        msg.setStandardButtons(QMessageBox.Ok)
                        result = msg.exec_()
                        if result == QMessageBox.Ok:
                            self.true = False
                else:
                        pass
                    

# 메인에서 실행해줍니다. 
app = QApplication(sys.argv)
ex = MyApp()
ex.check_alarm()
sys.exit(app.exec_())