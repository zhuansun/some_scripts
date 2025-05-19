import time
import requests
import json

# 定义目标URL
url = "https://hwapi.vip.cpolar.cn/hw/hello/check"
notifyUrl1 = "https://api.day.app/MuZnemfDhYUswqbjCXCgBd/HelloPanError/CheckError111"
notifyUrl2 = "https://api.day.app/MuZnemfDhYUswqbjCXCgBd/HelloPanError/Check222"

while True:
    # 当前线程休眠1分钟
    time.sleep(60)
    # 发起网络请求
    response = requests.get(url)
    print(response.text)
    # 解析返回的JSON数据
    try:
        response_data = json.loads(response.text)
        # 如果返回的code为200且data为true，则认为系统正常
        if response_data.get("code") == 200:
            print("系统正常")
        else:
            requests.get(notifyUrl1)
    except json.JSONDecodeError:
        print("返回的数据不是有效的JSON格式")
        requests.get(notifyUrl2)