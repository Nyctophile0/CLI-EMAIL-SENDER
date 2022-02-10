import os
from sys import platform
import time
from termcolor import cprint
import smtplib
from email.message import EmailMessage
import getpass
import pwinput
from email_validator import validate_email, EmailNotValidError
import pyfiglet

def emailvalidate(email):

    try:
        validate_email(email)
    except EmailNotValidError as e:
        print(str(e))
        exit(1)

def emailauthentication(email, password):

    try:
        smtplib.SMTP_SSL('smtp.gmail.com', 465).login(email, password)
    except smtplib.SMTPAuthenticationError:
        print('Invalid username/password.')
        exit(1)

def head():
    time.sleep(0.5)

    if platform == 'win32':
        os.system('cls')
    elif platform == 'linux':
        os.system('clear')

    cprint(pyfiglet.figlet_format("\tCONSOLE EMAIL SENDER", font='digital'), 'green', attrs=['bold'])

def progress():
    r = 40
    items = list(range(0, r))
    l = len(items)
    for i, item in enumerate(items):
        time.sleep(0.02)
        filled = int(r * (i + 1) // l)
        bar = '█' * filled + ' ' * (r - filled)
        print(f'\r{bar}', end='\r')

def sendemail(sender, password, message, reciever, subject):

    msg = EmailMessage()
    msg['subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        print('\nAuthenticating... ')
        smtp.login(sender, password)

        print('Sending mail... ')
        sent = smtp.send_message(msg)

        cprint('\nEmail Sent Succesfully!', 'green', attrs=['bold'])
        exit(1)

'''def animation():

    animat = '|/-'
    idx = 0

    while True:
        print(animat[idx % len(animat)], end="\r")
        idx += 1
        time.sleep(0.1)

        if idx == 10:
            break'''

def main():
    while True:
        print('\nSend email (1)\nExit (2)')
        choice = input('\nEnter: ')
        if choice == '2':
            print("\nExiting program ...\nExited!")
            exit(1)
        elif choice == '1':
            print('\nSend email through default Email(1)\nSend email through another Email(2)')
            choice2 = input('\nEnter: ')
            if choice2 == '1':
                cprint('\n*Sending email through default email*', attrs=['bold'])
                print('\nExtracting credentials ..\nExtracted!')
                sender = os.environ.get('EMAIL_USER')
                pas = os.environ.get('EMAIL_PASS')

                print(f"\nYour email address: {sender}")

                ans = input("\nIf you want to send email through this email press 'y' else 'n': ")

                if ans == 'y':

                    reciever = input("\nEnter reciever's email address: ")

                    emailvalidate(reciever)

                    subject = input("Enter subject of the email: ")
                    message = input("Enter content: ")

                    sendemail(sender, pas, message, reciever, subject)

                elif ans == 'n':
                    print("\n1.Send mail through different email\n2.Exit")

                    choice = input("\nEnter: ")

                    if choice == '1':
                        sender_email = input("\nEnter Email address: ")

                        emailvalidate(sender_email)

                        sender_password = pwinput.pwinput("Enter password: ")
                        confirm_password = pwinput.pwinput("Confirm password: ")

                        if not sender_password == confirm_password:
                            print("\nPasswords don't match!")
                            exit(1)

                        print("\nVerifying details ..")
                        emailauthentication(sender_email, sender_password)
                        print("Verified!")

                        reciever = input("\nEnter reciever's email address: ")

                        emailvalidate(reciever)

                        subject = input("Enter subject of the email: ")
                        message = input("Enter content: ")

                        sendemail(sender_email, sender_password, message, reciever, subject)

                    elif choice == '2':
                        print("\nExiting program ..\n Exited!")
                        exit(1)

                    else:
                        print("Wrong choice!")

                else:
                    print("Wrong choice!")

            elif choice2 == '2':
                sender_email = input("\nEnter Email address: ")

                emailvalidate(sender_email)

                sender_password = pwinput.pwinput("Enter password: ")
                confirm_password = pwinput.pwinput("Confirm password: ")

                if not sender_password == confirm_password:
                    print("\nPasswords don't match!")
                    exit(1)

                print("\nVerifying details ..")
                emailauthentication(sender_email, sender_password)
                print('Verified!')

                reciever = input("\nEnter reciever's email address: ")

                emailvalidate(reciever)

                subject = input("Enter subject of the email: ")
                message = input("Enter content: ")

                sendemail(sender_email, sender_password, message, reciever, subject)

            else:
                cprint('Wrong choice!!', 'red', attrs=['bold'])
        else:
            cprint('Wrong choice!', 'red', attrs=['bold'])

if __name__ == '__main__':
    head()
    progress()
    print()
    main()
