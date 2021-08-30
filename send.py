# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:41:00 2019

"""
    
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

#filepath = r"""C:\Users\username\Desktop\library\logg.zip"""
# address = ''
# password = ''
# mail_adr = ''
# mail_port = 465

# Compose attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filepath))

# Compose message
msg = MIMEMultipart()
msg['From'] = address
#msg['To'] = ""
msg.attach(part)

# Send mail
smtp = SMTP_SSL()
smtp.connect(mail_adr, mail_port)
smtp.login(address, password)
smtp.sendmail(address, address, msg.as_string())
smtp.quit()