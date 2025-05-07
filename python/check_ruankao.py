import time
import requests
from bs4 import BeautifulSoup

# 定义目标URL和Cookies
url = "https://bm.ruankao.org.cn/query/score/main"
cookies = {'Cookie': 'PHPSESSID=s40itd5639shq98b9513124de7; ZhuoFanRuanKaoUserRegID=2403082126327201042467204; acw_tc=2f6a1fc617337959220947155ed07abb4389038fefcb290d55202bdb9cf6dd; SERVERID=4fe3fb57dac5111ac659e698b82916c7|1733796802|1733794101'}

while True:
    # 当前线程休眠1分钟
    # time.sleep(600)
    print("开始请求")
    # 发起网络请求
    response = requests.get(url, headers={'Cookie': cookies['Cookie']})
    print(response.text)
    # 确保请求成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到目标select标签并提取option内容
        options = soup.select(".input-block.drop select#stage option")
        option_values = [option.text.strip()
                         for option in options if option.text.strip()]
        # 输出结果
        print(option_values)
        if "2024年下半年" in option_values:
            print("2024年下半年考试")
            # requests.get(f"https://api.day.app/Bd/成绩出来了")
            break
