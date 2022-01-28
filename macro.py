import os
import sys
import time
import threading
import datetime
import json
import webbrowser
from playsound import playsound

# 시각 구하기
dy_lis = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

xc = datetime.datetime.now()
t = time.localtime()
yr = str(t.tm_year) # 년
mo = str(t.tm_mon) # 월
dt = str(t.tm_mday) # 일
dy = dy_lis[t.tm_wday]

now_time = time.strftime("%H:%M", t)

# 알람 울릴 시간 구하기
full_next_time = '20221280924'
full_next_time = datetime.datetime.strptime(full_next_time, "%Y%m%d%H%M")
print(mo)
print(now_time)
print(full_next_time)

min_left = full_next_time - xc
min_left = min_left.seconds/60
print(min_left)

# 수업 접속하기
subject = '인터뷰'
professor = '토마토'
id = '83966708197'
pw = 'snuroedm'
url = 'zoommtg://zoom.us/join?confno={}&pwd={}'.format(id, pw)

# 수업에 접속하기
if 0 <= min_left <= 5:
    webbrowser.open(url)
    playsound('sounds/alarm.wav', block=False)
elif 10 <= min_left < 11:
    pass
else:
    pass

# 요일 일치

# 시간 일치

# 분 일치 or 5분 전이면 소리 울리기


# load data

# https://kimdonghee.dev/posts/Programs_Utility_Auto-Participate-in-Zoom/