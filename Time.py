import time, datetime

tm = time.localtime(time.time())
print("year:", tm.tm_year)
print("month:", tm.tm_mon)
print("day:", tm.tm_mday)
print("hour:", tm.tm_hour)
print("minute:", tm.tm_min)
print("second:", tm.tm_sec)

def get_today_days():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return days[datetime.datetime.today().weekday()]

print(get_today_days())

# 시간 분까지 일치하면 굿 :ㅇ
