# 调试 日志输出
import logging
logging.basicConfig(level=logging.INFO)

def fn():
	logging.info("方法进入了")
	a,b,c = 1,2,3
	d=c/a
	print(int(d))
	return

fn()