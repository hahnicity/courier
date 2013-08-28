"""
courier.mailer
~~~~~~~~~~~~~~
"""
from getpass import getpass
from smtplib import SMTP


def get_server(hostname, username):
    """
    Initialize a mailing server we wish to use
    """
    server = SMTP(hostname)
    server.starttls()
    password = getpass("Enter you password for {}:".format(username))
    server.login(username, password)
    return server


def send_mail(server, from_, send_to, message):
    """
    Send a piece of mail to a list of recipients
    """
    server.sendmail(from_, send_to, message)
    server.quit()
