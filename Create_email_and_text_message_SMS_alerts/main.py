import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to_address):
    email_msg = EmailMessage()
    email_msg.set_content(body)
    email_msg['subject'] = subject
    email_msg['to'] = to_address


    user = 'kndristy@gmail.com'
    email_msg['from'] = user
    password = 'rijycmnygjuqkttg'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(email_msg)

    server.quit()

if __name__ == '__main__':
    email_alert('Important', 'Ei room e ayy !! ', 'aarafi2000@gmail.com')
    print("Email Sent Successfully")
