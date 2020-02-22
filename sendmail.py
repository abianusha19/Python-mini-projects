import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

mailid='somuumos@gmail.com'
password='somusomu123'
tolist=['thapavithra@gmail.com','rupashri119@gmail.com','abianusha1950@gmail.com']

for x in tolist:
  server=smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
 

  server.login(mailid,password)

  message=MIMEText('Sent from py code')
  message=MIMEMultipart()
  message["From"]=mailid
  message["To"]=x
  message["Subject"]='hi this is abi '
  body="Hi hello everyone.. This is a sample.."
  message.attach(MIMEText(body,'plain'))
  filename="images.jpg"
  attachment=open(filename,"rb")
  p=MIMEBase('application','octet-stream')
  p.set_payload((attachment).read())
  encoders.encode_base64(p)
  p.add_header('Content-Disposition',"attachment;filename=%s" % filename)
  message.attach(p)
  server.sendmail(mailid,x,message.as_string())
  server.quit()
print("Mail sent Successfully")