from datetime import datetime,timedelta

# 获取当前时间
print(datetime.now())

# 获取指定时间
print(datetime(2015,4,19,12,20))

# 获取时间戳
print(datetime(2015,4,19,12,20).timestamp())

# 时间戳转时间
t = datetime.now().timestamp()
print(datetime.fromtimestamp(t))

# 时间戳转UTC时间
print(datetime.utcfromtimestamp(t))

# string转时间
print(datetime.strptime('2019-03-11 15:20:09','%Y-%m-%d %H:%M:%S'))

# 时间转string
print(datetime.now().strftime('%H:%M:%S'))

# 加减时间
print(datetime.now() + timedelta(hours=3))
print(datetime.now() - timedelta(days=3))



