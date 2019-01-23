import smtplib

sender = 'keegan0415dsouza@gmail.com'
receivers = ['keegan0415dsouza@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
print("hello")
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except Exception as e:
   print ("Error: unable to send email")