from email.message import EmailMessage
from decouple import config
import ssl
import smtplib

# Organizar el codigo, limpiarlo y realizar buenas practicas
def send_email(to_line, subject_line, body_text):
        
    port = 465
    smtp_server = "smtp.gmail.com"
    email_sender = 'pruebasjos1@gmail.com'
    password = config("EMAIL_PASSWORD")

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = to_line
    em['subject'] = subject_line 
    em.set_content(body_text)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(email_sender, password) 
        smtp.sendmail(email_sender, to_line, em.as_string())
