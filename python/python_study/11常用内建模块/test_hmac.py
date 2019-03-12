import hmac

message = b'hello world'
key = b'slat'
h = hmac.new(key,message,digestmod='MD5')
# 如果消息过长，可以多次调用 h.update(msg)
print(h.hexdigest())
