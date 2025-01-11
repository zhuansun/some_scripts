import os
import requests



# 指令目录路径
base_path = '/Users/zhuansunpengcheng/Downloads/未命名文件夹'

# 读取指令目录下的所有文件
paths = [os.path.join(base_path, f) for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]



for pathItem in paths:
    # 指令目录路径
    directory_path = pathItem

    print('开始处理-------------'+directory_path)

    # 读取指令目录下的所有文件
    files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # 用于保存成功的请求
    success_records = []
    # 用于保存异常的请求
    exception_records = []

    # 遍历文件数组，上传文件
    for file_path in files:
        try:
            # 构建请求数据
            files = {'file_up': open(file_path, 'rb')}
            data = {
                'csrf': 'f35a0df142101638fb62908aaba490b1',
                'biz': 'article'
            }
            headers = {
                'Cookie': "buvid3=2796284F-4E77-49FE-7B53-5C68B5E30C1A48943infoc; b_nut=1726238248; _uuid=88CB37DB-C732-29A2-49C10-444D106A18F10249115infoc; buvid4=E1E41E72-36CA-29CB-E204-311B320F860D49850-024091314-e8lYtddN14jsPX3jDrBKcw%3D%3D; header_theme_version=CLOSE; enable_web_push=DISABLE; DedeUserID=347779649; DedeUserID__ckMd5=f97fc1794b64d131; rpdid=|(Y|lJu|)lY0J'u~kYYY|m)J; fingerprint=afd807ea97659456e0ae06fb9d402689; buvid_fp_plain=undefined; buvid_fp=afd807ea97659456e0ae06fb9d402689; CURRENT_BLACKGAP=0; home_feed_column=5; bp_t_offset_347779649=1007845231699165184; CURRENT_QUALITY=80; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ5NjA5MTMsImlhdCI6MTczNDcwMTY1MywicGx0IjotMX0.8JCRfjUENwzJ4mNiQ0jYB8DXUpNCOwkHjPvnEfUTOAE; bili_ticket_expires=1734960853; b_lsid=4CD411097_193E4636043; SESSDATA=ee82a86e%2C1750255539%2Cffa5d%2Ac1CjATcu3cAkw5y55-Y2S3xmG299rZT3_A47eUGPDqwbUZHvaAn2I4iH71YK1dzfnAlcISVnNFbXY1c0JPLVJackpYR3haWTY2NmRGTW9wMWJBYjJTT2FTRlJoZ3oxdERVQVpnRjBuMEc4aVoyc0VFa2lYN3YwU0lQZWItTmNVeW40Zk9YNXJaSllBIIEC; bili_jct=f35a0df142101638fb62908aaba490b1; sid=6s9j13lo; browser_resolution=1512-428"
            }
            # 设置超时时间为20秒
            timeout = 20
            
            # 发送请求
            response = requests.post('https://api.bilibili.com/x/dynamic/feed/draw/upload_bfs', 
                                    headers=headers, 
                                    files=files, 
                                    data=data,
                                    timeout=timeout)
            
            # 检查响应状态
            if response.status_code == 200 and response.json()['code'] == 0:
                # 请求成功，记录文件名和imageUrl
                success_records.append({
                    'file_name': os.path.basename(file_path),
                    'image_url': response.json()['data']['image_url']
                })
                print(f"Success: {os.path.basename(file_path)} - {response.json()['data']['image_url']}")
            else:
                # 请求异常，记录文件名
                exception_records.append(os.path.basename(file_path))
                print(f"Exception: {os.path.basename(file_path)}" + response)
        except Exception as e:
            # 记录异常请求的文件名
            exception_records.append(os.path.basename(file_path))
            print(f"Exception: {os.path.basename(file_path)} - Error: {e}")

    # 输出成功的请求记录
    # print("\nSuccessful uploads:")
    resultList = []
    for record in success_records:
        # print(f"File: {record['file_name']}, Image URL: {record['image_url']}")
        resultList.append((record['file_name'], record['image_url']))

    # 输出异常的请求记录
    print("\nException uploads:")
    for file_name in exception_records:
        print(f"File: {file_name}")


    # 按照文件名排序
    resultList.sort(key=lambda x: x[0])

    # 输出排序后的图片URL
    for result in resultList:
        # print(file)
        print(pathItem + " = " +result[1])