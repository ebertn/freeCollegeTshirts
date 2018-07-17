import csv
import smtplib
from email.message import EmailMessage
import time

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')

        return 1
    except Exception as e: 
        print(e)
        print("failed to send mail")

    return 0

if __name__ == '__main__':
    with open('formatted_colleges.csv') as f:
        reader = csv.reader(f)
        colleges = list(reader)

    # TODO: Your gmail
    fromaddr = "person@gmail.com"

    # TODO: Put password here (hunter12 is not my password fyi)
    password = "hunter12" 

    # TODO: Optional - this is the subject of the email. Hello works just fine
    sub = "Hello"

    sent = 1

    for college, email in colleges:
        if sent == 1:
            college = college[:-1]

            # TODO: Edit you info here (name, high school, GPA, shipping address, t-shirt size, name again)
            body = f"Dear {college},\n\nMy name is Nick and I am very interested in applying this fall to {college} to be a student! I attend Saline High School in Saline, Michigan, have a 3.87 GPA, and am on the honor roll.\n\nI would love to have a T-shirt to represent {college}; can you send me one? My address is 358 Aberdeen Ct., Saline, MI. I wear a size large (L).\n\nThank you,\n\nNick"
            sent = send_email(fromaddr, password, email, sub, body)
            print(college)
        else:
            time.sleep(120)
            print("Restarting")

            # TODO: Edit you info here (name, high school, GPA, shipping address, t-shirt size, name again)
            body = f"Dear {college},\n\nMy name is Nick and I am very interested in applying this fall to {college} to be a student! I attend Saline High School in Saline, Michigan, have a 3.87 GPA, and am on the honor roll.\n\nI would love to have a T-shirt to represent {college}; can you send me one? My address is 358 Aberdeen Ct., Saline, MI. I wear a size large (L).\n\nThank you,\n\nNick"
            sent = send_email(fromaddr, password, email, sub, body)
            print(college)


