from decouple import config
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

MY_ADRESS = config("MY_ADRESS")
PASSWORD = config('PASSWORD')
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADRESS, PASSWORD)
names, emails = get_contacts('mycontacts.txt')  
message_template = read_template('message.txt')

for name, email in zip(names, emails):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title())
    msg['From']="francosbenitez@gmail.com"
    msg['To']="francosbenitez@gmail.com"
    msg['Subject']="This is TEST"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg

