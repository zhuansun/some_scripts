import re

# 原始文本
text = """
File: IMG4537.JPG, Image URL: http://i0.hdslb.com/bfs/article/5565be7922db67a1a7e4f5b1fe1ba26d347779649.jpg
File: IMG4523.JPG, Image URL: http://i0.hdslb.com/bfs/article/ac4923909cc8f11bd5e7472800c1e213347779649.jpg
File: IMG4522.JPG, Image URL: http://i0.hdslb.com/bfs/article/5304f2a26b61dbb5dda55071b4ab423d347779649.jpg
File: IMG4536.JPG, Image URL: http://i0.hdslb.com/bfs/article/e27e3e1babf9f72f657ec32483ea44e0347779649.jpg
File: IMG4520.JPG, Image URL: http://i0.hdslb.com/bfs/article/9485245c7f5ac006cb6cacdd029abef6347779649.jpg
File: IMG4534.JPG, Image URL: http://i0.hdslb.com/bfs/article/3dd08364acd8f031a32458f5851c29d0347779649.jpg
File: IMG4509.jpg, Image URL: http://i0.hdslb.com/bfs/article/b943a946117ade81ad51042c3a7be7af347779649.jpg
File: IMG4535.JPG, Image URL: http://i0.hdslb.com/bfs/article/5003e4739820dbfe719fd983d422f7ac347779649.jpg
File: IMG4521.JPG, Image URL: http://i0.hdslb.com/bfs/article/62e4e92490e6bd6cf146776b554035a2347779649.jpg
File: IMG4519.JPG, Image URL: http://i0.hdslb.com/bfs/article/e1e8759fdc4bc480eda9415bce34da5a347779649.jpg
File: IMG4525.JPG, Image URL: http://i0.hdslb.com/bfs/article/58101abe5dfdd93fac82f46498f67f79347779649.jpg
File: IMG4531.JPG, Image URL: http://i0.hdslb.com/bfs/article/dc24ff74d393dd30f34e7b9fec89a021347779649.jpg
File: IMG4530.JPG, Image URL: http://i0.hdslb.com/bfs/article/1044dccca364aa923715c21361cda679347779649.jpg
File: IMG4524.JPG, Image URL: http://i0.hdslb.com/bfs/article/76680b0343cb5d36fd299a5a618740a1347779649.jpg
File: IMG4518.JPG, Image URL: http://i0.hdslb.com/bfs/article/a6434ccaff204da081d1a0801e5f6dbe347779649.jpg
File: IMG4532.JPG, Image URL: http://i0.hdslb.com/bfs/article/af3cbbbad4eb79c73528d31361000d97347779649.jpg
File: IMG4526.JPG, Image URL: http://i0.hdslb.com/bfs/article/aa8023517d1e89453175df7459b9463f347779649.jpg
File: IMG4527.JPG, Image URL: http://i0.hdslb.com/bfs/article/a09e3e11e5c78ef8eede54b6d1f78ac6347779649.jpg
File: IMG4533.JPG, Image URL: http://i0.hdslb.com/bfs/article/e7048a88f98c2a9119469cac0cdee390347779649.jpg
File: IMG4540.JPG, Image URL: http://i0.hdslb.com/bfs/article/7efa2805eabadbf8fd5e5ddafcb36023347779649.jpg
File: IMG4541.JPG, Image URL: http://i0.hdslb.com/bfs/article/466254d8fdd9407fba85d72dd6a4297b347779649.jpg
File: IMG4543.JPG, Image URL: http://i0.hdslb.com/bfs/article/d6faaca7e1669a120ef289705a55b4ef347779649.jpg
File: IMG4542.JPG, Image URL: http://i0.hdslb.com/bfs/article/93b11972f3b6ae20c0cdc4a6ca474e66347779649.jpg
File: IMG4546.JPG, Image URL: http://i0.hdslb.com/bfs/article/04f3248ae568e04dcbbde0f493c72470347779649.jpg
File: IMG4547.JPG, Image URL: http://i0.hdslb.com/bfs/article/de2dd5f6cfe4b9edcb95f97a86071d89347779649.jpg
File: IMG4551.JPG, Image URL: http://i0.hdslb.com/bfs/article/a1539a56401110dafffd7e759a854c3b347779649.jpg
File: IMG4545.JPG, Image URL: http://i0.hdslb.com/bfs/article/b894687cd06a15a7d76e7716513a3956347779649.jpg
File: IMG4544.JPG, Image URL: http://i0.hdslb.com/bfs/article/2dd2d9f059241395c61a8d5f6562e47f347779649.jpg
File: IMG4550.JPG, Image URL: http://i0.hdslb.com/bfs/article/1f196d48829df18149b2cbb9847b8eac347779649.jpg
File: IMG4549.JPG, Image URL: http://i0.hdslb.com/bfs/article/647402b3a77d1b93e3c396a51e92278e347779649.jpg
File: IMG4516.JPG, Image URL: http://i0.hdslb.com/bfs/article/b391b8ae0c05e5a1ec40bd52edef4223347779649.jpg
File: IMG4517.JPG, Image URL: http://i0.hdslb.com/bfs/article/680243b0ec8037829aac44ec01df331e347779649.jpg
File: IMG4515.JPG, Image URL: http://i0.hdslb.com/bfs/article/fcc6967c5a4484c642a13d68263f916f347779649.jpg
File: IMG4529.JPG, Image URL: http://i0.hdslb.com/bfs/article/136a6ac60680b12c0d384353727fbbc7347779649.jpg
File: IMG4528.JPG, Image URL: http://i0.hdslb.com/bfs/article/c4f86005bc54a4bba9413c83d78c0fec347779649.jpg
File: IMG4514.JPG, Image URL: http://i0.hdslb.com/bfs/article/dc4372d55252caa3584c3bfa0f81e173347779649.jpg
File: IMG4538.JPG, Image URL: http://i0.hdslb.com/bfs/article/93e9d547d5fa30e03488789112fc47d8347779649.jpg
File: IMG4539.JPG, Image URL: http://i0.hdslb.com/bfs/article/5273e6f64f13eb9088f7872d46a1510d347779649.jpg
File: IMG4513.JPG, Image URL: http://i0.hdslb.com/bfs/article/273335b1a70d7e5ee2f489ec11537528347779649.jpg
File: IMG4512.JPG, Image URL: http://i0.hdslb.com/bfs/article/9b8dc14e0c3e1c45e577a304a4bb6340347779649.jpg
"""

# 使用正则表达式匹配文件名和图片URL
pattern = r"File: (.*?), Image URL: (http://.*?\.jpg)"
matches = re.findall(pattern, text)

# 将匹配结果存储到列表中
files = []
for match in matches:
    files.append((match[0], match[1]))

# 按照文件名排序
files.sort(key=lambda x: x[0])

# 输出排序后的图片URL
for file in files:
    # print(file)
    print(file[1])