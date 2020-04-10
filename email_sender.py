import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'Sender'
email['to'] = 'receiver_email'
email['subject'] = 'you won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Aditya'}), 'html')

print(html.substitute({'name': 'Aditya'}))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email_acc', 'acc_password')
    smtp.send_message(email)
    print('email sent')