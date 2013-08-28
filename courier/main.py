"""
courier.main
~~~~~~~~~~~~
"""
#!/usr/bin/env python
from argparse import ArgumentParser

from courier.defaults import MAIL_SERVER
from courier.mailer import get_server, send_mail


def parse_argv():
    """
    Parse command line arguments
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--hostname",
        help=("The name of the mail server we want"
              " to point to. default: {}".format(MAIL_SERVER)),
        default=MAIL_SERVER
    )
    parser.add_argument(
        "-s",
        "--sender",
        help=("The mailing address we want to send our email(s) from")
    )
    parser.add_argument(
        "-r",
        "--recipients",
        help=("A list of mailing addresses to send our message to"),
        nargs="*"
    )
    parser.add_argument(
        "-m",
        "--message",
        help=("A message to send.")
    )
    return parser.parse_args()


def main():
    """
    Console script for courier
    """
    args = parse_argv()
    server = get_server(args.hostname, args.sender.split("@")[0])
    send_mail(server, args.sender, args.recipients, args.message)


# For dev purposes
if __name__ == "__main__":
    main()
