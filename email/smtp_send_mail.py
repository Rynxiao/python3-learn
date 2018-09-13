#!/usr/bin/env python3

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

def _format_addr(s):
  name, addr = parseaddr(s)
  return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令
# from_addr = input('From:')
# password = input('Password:')
# 输入收件人地址：
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

from_addr = '1060941832@qq.com'
password = 'undwasuhnttnbdbe'
to_addr = 'yuzhongzi91@sina.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 带网页的邮件消息
html_msg = MIMEText('<html><body><h1>Hello</h1>' +
  '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
  '</body></html>', 'html', 'utf-8')
html_msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
html_msg['To'] = _format_addr('管理员 <%s>' % to_addr)
html_msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 带附件的邮件消息
attach_msg = MIMEMultipart()
attach_msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
attach_msg['To'] = _format_addr('管理员 <%s>' % to_addr)
attach_msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
# attach_msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 邮件正文是带有附件的Text
attach_msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
  '<p><img src="cid:0"></p>' +
  '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('./thumbnail.png', 'rb') as f:
  # 设置附件的MIME和文件名，这里是png类型:
  mime = MIMEBase('image', 'png', filename='meinv.png')
  # 加上必要的头信息:
  mime.add_header('Content-Disposition', 'attachment', filename='meinv.png')
  mime.add_header('Content-ID', '<0>')
  mime.add_header('X-Attachment-Id', '0')
  # 把附件的内容读进来:
  mime.set_payload(f.read())
  # 用Base64编码:
  encoders.encode_base64(mime)
  # 添加到MIMEMultipart:
  attach_msg.attach(mime)


import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], attach_msg.as_string())
server.quit()