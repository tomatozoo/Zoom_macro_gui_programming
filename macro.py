import os
import sys
import time
import threading
import datetime
import json
import webbrowser

# 시각 구하기
dy_lis = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

xc = datetime.datetime.now()
t = time.localtime()
yr = str(t.tm_year)
mo = str(t.tm_mon)
dt = str(t.tm_mday)
dy = dy_lis[t.tm_day]

now_time = time.strftime("%H%M", t)

# load data

# https://kimdonghee.dev/posts/Programs_Utility_Auto-Participate-in-Zoom/