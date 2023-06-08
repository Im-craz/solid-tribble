from email.message import EmailMessage
from password import email_password
import ssl
import smtplib


email_sender = 'pruebasjos1@gmail.com'
email_receiver = 'josethnarvaez3506@gmail.com'
subject = 'Saludo'
body = '''
Buena noche, un saludo si funciona!!
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
