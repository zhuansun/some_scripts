from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = input('From: xxxx@xx.com')
password = input('Password: xxxxx')
# 输入收件人地址:
to_addr = input('To: xxxx@xx.com')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: xxx.xxx.xxx')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()