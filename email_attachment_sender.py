import os
import sys
import smtplib
import mimetypes
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email_validator import validate_email, EmailNotValidError
import pwinput
from termcolor import cprint

def emailauthentication(email, password):

    try:
        smtplib.SMTP_SSL('smtp.gmail.com', 465).login(email, password)
    except smtplib.SMTPAuthenticationError:
        cprint('Invalid username/password.', 'red', attrs=['bold'])
        exit(1)

def emailvalidate(email):

    try:
        validate_email(email)
    except EmailNotValidError as e:
        cprint(str(e), 'red', attrs=['bold'])
        exit(1)

def send(password, sender, reciever, subject, body, filepath=None):

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = reciever
    msg['Subject'] = subject
    msg['body'] = body
    msg.attach(MIMEText(body, 'plain'))

    for file in filepath or []:
        with open(file, "rb") as fp:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((fp).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename= %s' %os.path.basename(file))
            msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        print('\nLogging in ..')
        smtp.login(sender, password)
        print("Logged in!")

        text = msg.as_string()
        print('\nUploading file(s) and Sending mail ..')
        cprint('\n***UPLOADING FILES MAY TAKE SOME TIME DEPENDS ON FILE SIZE***', 'green')
        smtp.send_message(msg)

    print('\nMail Sent.')

def main():

    filepath = []

    email = input("Sender's Email: ")
    emailvalidate(email)

    password = pwinput.pwinput("Password: ")

    print("\nVerifying details ..")
    emailauthentication(email, password)
    print("Verified!\n")

    reciever = input("Reciever's Email: ")
    emailvalidate(reciever)

    subject = input("\nSubject: ")
    body = input("Body: ")

    cprint("\nNote - You can send up to 25 MB in attachments.", 'green')
    cprint("        If you have more than one attachment, ", 'green')
    cprint("        they can't add up to more than 25 MB.", 'green')

    filepath.append(input("\nFile path(without any inverted commas): "))
    print('File added to the list.')

    while True:

        choice = input('\nDo you want to add more files(y/n): ')
        if choice in ['y', 'Y', 'yes', 'Yes', 'YES']:
            filepath.append(input("File path(without any inverted commas): "))
            print('Another file added to list.')
        elif choice in ['n', 'N', 'No', 'NO', 'no']:
            break
        else:
            cprint('Wrong choice', 'red')

    send(password, email, reciever, subject, body, filepath)

if __name__ == "__main__":

    os.system('cls')
    main()

