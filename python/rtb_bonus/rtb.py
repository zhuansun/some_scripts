import requests
from datetime import datetime, timedelta
import json



class DataObject:
    def __init__(self, dataStr, mobileCount, mobleStore, vipMoney, source):
        self.dataStr = dataStr
        self.mobileCount = mobileCount
        self.mobleStore = mobleStore
        self.vipMoney = vipMoney
        self.source = source

    def __repr__(self):
        return f"DataObject(dataStr={self.dataStr}, mobileCount={self.mobileCount}, mobleStore={self.mobleStore}, vipMoney={self.vipMoney}, source={self.source})"

def method1(data, source):
    # 创建一个空列表来存储解析后的对象
    result_objects = []
    
    # 将字符串转换为字典
    data_dict = json.loads(data)
    
    # 遍历data中的list部分
    for item in data_dict['data']['list']:
        # 解析对象
        data_object = DataObject(
            dataStr=item['date_str'],
            mobileCount=item['u_count1'],
            mobleStore=item['u_count2'],
            vipMoney=item['u_money3'],
            source=source
        )
        # 将解析后的对象添加到列表中
        result_objects.append(data_object)
    
    return result_objects

def method2(data, source):
    # 创建一个空列表来存储解析后的对象
    result_objects = []
    
    # 将字符串转换为字典
    data_dict = json.loads(data)
    
    # 遍历data中的list部分
    for item in data_dict['data']['list']:
        # 解析对象
        data_object = DataObject(
            dataStr=item['date_str'],
            mobileCount=item['mobile_count'],
            mobleStore=item['store_count'],
            vipMoney=item['mobile_fencheng'],
            source=source
        )
        # 将解析后的对象添加到列表中
        result_objects.append(data_object)
    
    return result_objects


# 目标 URL
baiduUrl = 'https://dt.bd.cn/main/baidupan_list'
quarkUrl = 'https://dt.bd.cn/main/quark_list'

bsList = [
    {"type":"BAIDU","bs":"4236298918"},
    {"type":"QUARK-1","bs":"100187470341"},
    {"type":"QUARK-2","bs":"100676748675"}
]

# 请求头
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Cookie
cookies = {
    'PHPSESSID': 'v9g20g7qema86f86d6t4md5gh0',
    'SERVERID': '60db755fec3430d627f0ed585eca91ed|1734521355|1734521355',
    'acw_tc': '0b32807e17345213555523488e53eb29ae1ab7e19bfaa42afbe9dbc2142f59'
}

# 获取当前时间
current_date = datetime.now()

# 获取当前时间的前20天
start_date = current_date - timedelta(days=10)

# 格式化日期为 YYYY-MM-DD
formatted_start_date = start_date.strftime('%Y-%m-%d')
formatted_end_date = current_date.strftime('%Y-%m-%d')

# POST 请求的数据模板
data_template = {
    'start_date': formatted_start_date,
    'end_date': formatted_end_date
}

result_list = []

# 遍历 bsList
for item in bsList:
    # 根据 type 设置 data 中的 bs
    # 复制数据模板
    data = data_template.copy()
    data['bs'] = item["bs"]

    try:
        if "BAIDU" in item["type"]:
            # 发起 POST 请求
            response = requests.post(baiduUrl, headers=headers, cookies=cookies, data=data)
            # 调用 method1 处理 response.text，结果放进result_list中
            result_list.extend(method1(response.text, item["type"]))
        elif "QUARK" in item["type"]:
            # 发起 POST 请求
            response = requests.post(quarkUrl, headers=headers, cookies=cookies, data=data)
            # 调用 method2 处理 response.text，结果放进result_list中
            result_list.extend(method2(response.text, item["type"]))
    except requests.RequestException as e:
        print(f"请求错误: {e}")

# 打印结果resuleList的json
print(json.dumps(result_list, default=lambda o: o.__dict__, ensure_ascii=False))
