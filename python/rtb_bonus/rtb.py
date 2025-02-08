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

    def to_dict(self):
        return {
            "dataStr": self.dataStr,
            "mobileCount": self.mobileCount,
            "mobleStore": self.mobleStore,
            "vipMoney": self.vipMoney,
            "source": self.source
        }

    def __repr__(self):
        return f"DataObject(dataStr={self.dataStr}, mobileCount={self.mobileCount}, mobleStore={self.mobleStore}, vipMoney={self.vipMoney}, source={self.source})"


def method1(data):
    result_objects = []
    data_dict = json.loads(data)
    for item in data_dict['data']['list']:
        data_object = DataObject(
            dataStr=item['date_str'],
            mobileCount=int(item['u_count1']),
            mobleStore=int(item['u_count2']),
            vipMoney=float(item['u_money3']),
            source='BAIDU'
        )
        result_objects.append(data_object)
    return result_objects


def method2(data):
    result_objects = []
    data_dict = json.loads(data)
    for item in data_dict['data']['list']:
        data_object = DataObject(
            dataStr=item['date_str'],
            mobileCount=int(item['mobile_count']),
            mobleStore=int(item['store_count']),
            vipMoney=float(item['mobile_fencheng']),
            source='QUARK'
        )
        result_objects.append(data_object)
    return result_objects


# 目标 URL
baiduUrl = 'https://dt.bd.cn/main/baidupan_list'
quarkUrl = 'https://dt.bd.cn/main/quark_list'

bsList = [
    {"type": "BAIDU", "bs": "4236298918"},
    {"type": "QUARK-1", "bs": "100187470341", "auth_key": "7c55ttOvyAu8n/VzfoxLrY3PFTB/IyC9BJjcal2+iUc9igYdPtrSlA"},
    {"type": "QUARK-2", "bs": "100676748675", "auth_key": "7c55ttOvyAu8n/VzfoxLrY3PFTB/IyC9BJjcal2+iUc9igYdPtrSlA"}
]

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded'
}

cookies = {
    'PHPSESSID': '37kvg1schqbmbu3barc1ohpau8',
    'SERVERID': '60db755fec3430d627f0ed585eca91ed|1738719331|1738719330',
    'acw_tc': '0b32807e17387193299811095e78361bf4324f0ce9a7e5d8b6afd282b0f7f2'
}

current_date = datetime.now()
start_date = current_date - timedelta(days=10)
formatted_start_date = start_date.strftime('%Y-%m-%d')
formatted_end_date = current_date.strftime('%Y-%m-%d')

data_template = {
    'start_date': formatted_start_date,
    'end_date': formatted_end_date
}

result_list = []
quark_data = []

for item in bsList:
    data = data_template.copy()
    data['bs'] = item["bs"]
    try:
        if item["type"] == "BAIDU":
            response = requests.post(baiduUrl, headers=headers, cookies=cookies, data=data)
            result_list.extend(method1(response.text))
        elif item["type"].startswith("QUARK"):
            data['auth_key'] = item["auth_key"]
            response = requests.post(quarkUrl, headers=headers, cookies=cookies, data=data)
            quark_data.extend(method2(response.text))
    except requests.RequestException as e:
        print(f"请求错误: {e}")

# 合并QUARK数据
merged_quark = {}
for obj in quark_data:
    key = obj.dataStr
    if key not in merged_quark:
        merged_quark[key] = {
            'mobileCount': 0,
            'mobleStore': 0,
            'vipMoney': 0.0,
            'source': 'QUARK'
        }
    merged_quark[key]['mobileCount'] += obj.mobileCount
    merged_quark[key]['mobleStore'] += obj.mobleStore
    merged_quark[key]['vipMoney'] += obj.vipMoney

# 添加合并后的QUARK数据到结果列表
for date_str, data in merged_quark.items():
    data_obj = DataObject(
        dataStr=date_str,
        mobileCount=data['mobileCount'],
        mobleStore=data['mobleStore'],
        vipMoney=data['vipMoney'],
        source=data['source']
    )
    result_list.append(data_obj)

# 将 result_list 转换为 JSON 字符串并打印
json_result = json.dumps([obj.to_dict() for obj in result_list], ensure_ascii=False)
print(json_result)