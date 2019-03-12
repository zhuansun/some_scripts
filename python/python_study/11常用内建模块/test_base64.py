import base64

a = "我是你爸爸"

print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))