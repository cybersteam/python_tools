#!/usr/bin/env python

#environment variables are stored in /etc/environment
#a google app password was created here: https://myaccount.google.com/apppasswords

#To setup a local debug server to test things like emails:
#python3 -m smtpd -c DebuggingServer -n localhost:1025
#then use localhost instead of smtp.gmail.com down below...

#we use os for the environment variables used in user and password
import os
#smtplib is for sending mail
import smtplib
#this is for formatting the message instead of the f statement further below
from email.message import EmailMessage
# module that detects what kind of image files is used
import imghdr

#define the from address and password - which are stored as environment variables
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_USER_PASS')

#to send to multiple recipients - need to make it ask for a spreadsheet or csv
contacts = ['infinite22@gmail.com', 'management@ivann.mobi']

msg = EmailMessage()
msg['Subject'] = 'subject of email'
msg['from'] = EMAIL_ADDRESS
msg['to'] = contacts
msg.set_content('body of messge')
#displays html in the mail - need to make it load an external html file and use that - user input
msg.add_alternative("""\
<!DOCTYPE html>
    <body>
        <h1>this</h1>
    </body>
</html>
""", subtype='html')

#define the attached image files list
files = ['pant.png', 'pant2.png']

#loop through this below with each file in "files"
for file in files:
#path to image and rb"read bytes"
    with open(file, 'rb') as f:
        file_data = f.read()
        #this line won't be needed for different file type only for image types
        file_type = imghdr.what(f.name)
        file_name = f.name
#for different file attachments use maintype='application' and subtype='octet-stream' (generic bag of bits type - python docs)
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

#using smtplib and it's module? SMTP pass the email obj and port - as variable we make called smtp
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(msg)
