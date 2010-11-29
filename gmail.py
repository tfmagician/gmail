#!/usr/bin/python
# -*- coding: utf-8 -*-

# import
import sys
import os
import smtplib
import yaml
import optparse
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

# globals
VERSION = '0.10'

def read_config(config_file):
    """
    Read configuration YAML file.

    account and password keys are required in the file.
    """

    config = yaml.load(open(config_file).read())
    not_exist = [setting for setting in ('account', 'password') if not config.has_key(setting)]
    if not_exist:
      print "Could not read %s setting from configration file." % ", ".not_exist 
      sys.exist(1)
    return config

def parse_options():
    """
    Parse options from arguments.
    """

    usage = "usage: %prog [-s subject] [-b body] to-addr..."
    ver = "%s %s" % ("%prog", VERSION)
    parser = optparse.OptionParser(usage, version=ver)
    parser.add_option("-s", "--subject", dest='subject',
                      default="",
                      metavar="STRING", help="Specify subject on command line")
    parser.add_option("-b", "--body", dest='body',
                      default="",
                      metavar="INPUT_FILE", help="Specify email body read from file")
    parser.add_option("-c", "--config", dest='config',
                      default="config.yaml",
                      metavar="INPUT_FILE", help="Setting file to use gmail server")
    opts, args = parser.parse_args()
    if args:
      for file in ('body', 'config'):
        if opts.__dict__[file] and not os.access(opts.__dict__[file], os.R_OK):
          print "Could not read %s from %s." % (file, opts.__dict__[file])
          sys.exit(1)
      return opts, args
    else:
      parser.print_help()
      sys.exit(0)

def create_message(from_addr, to_addrs, subject='', body='', encoding='utf-8'):
    """
    Create a mail body to send.
    """

    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = ",".join(to_addrs)
    msg['Date'] = formatdate()
    return msg

def send_via_gmail(account, passwd, to_addrs, msg):
    """
    Send an email through SMTP server of Gmail.
    """

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(account, passwd)
    s.sendmail(account, to_addrs, msg.as_string())
    s.close()

def main():
    """
    Main function.
    """

    opts, to_addrs = parse_options()
    settings = read_config(opts.config)
    if opts.body:
      opts.body = open(opts.body).read()
    msg = create_message(settings['account'], to_addrs, opts.subject, opts.body)
    send_via_gmail(settings['account'], settings['password'], to_addrs, msg)

if __name__ == '__main__':
    main()
