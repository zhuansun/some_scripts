from enum import Enum, unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sta = 6


# 访问枚举类
day1 = Weekday.Mon
print(day1) 

print(Weekday['Thu'])

print(Weekday['Sta'].value)

