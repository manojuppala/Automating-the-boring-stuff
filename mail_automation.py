import smtplib
import os
from email.message import EmailMessage
# SMTP stands for simple mail transfer protocol
smtpObj=smtplib.SMTP_SSL("smtp.gmail.com",465)
address=os.environ.get('EMAIL_USER')
password=os.environ.get('EMAIL_PASSWORD')
app=os.environ.get('APP_PASSWORD')

msg1=EmailMessage()
msg1['Subject']='Grab dinner this weekend'
msg1['From']=address
msg1['To']='uppala0863@gmail.com'
msg1.set_content('how about dinner 6pm this saturday.')
#to send a mail using the above format use send_message()
## smtp.send_message(msg1)
#if the the first element in the returned tuple is 250 then the connection is success
print(smtpObj.ehlo())
# the next step is to login into your gmail account
smtpObj.login(address,app)
#subjject of the mail
subject='Grab dinner thsi weekend?'
body='How about dinner at 6pm this saturday.'
#format the subjet and body togeather
msg=f'Subject: {subject}\n\n{body}'

smtpObj.sendmail(address,'uppala0863@gmail.com',msg)
#disconnecting from the smtp server
smtpObj.quit()

##if you want to create a local host on your computer you can do it using the following command
#open your terminal
#python -m smtpd -c DebuggingServer -n localhost:1025

## to automatically disconnect to the server you can use with-as to connect the server
# with smtplib.SMTP('localhost',1025) as smtp:
