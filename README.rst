gmail script by Python
======================

You can send an email through gmail SMTP server using this script.


Usage
-----

First install modules required (I'm using Ubuntu 10.04 TLS).::

    apt-get install -y libyaml-0-2 python-setuptools
    easy_install PyYAML

Second clone script on /etc, /usr/lib or somewhere you like.

    cd /path/to/dir
    git clone git://github.com/tfmagician/gmail.git

Third setup a configuration file to your account.

    cd gmail/
    cp config.yaml.example config.yaml
    vi config.yaml

Last you can send an email using this script.

    ./gmail.py --subject 'Hello world' --text --body 'Read me.' --config ./config.yaml wonder_land@sample.com

You will get an email from your server.


Options
-------

    --version             show program's version number and exit
    -h, --help            show this help message and exit
    -s STRING, --subject=STRING
                          Specify subject on command line
    -b INPUT_FILE, --body=INPUT_FILE
                          Specify email body read from file
    -t, --text            --body argument as text not file
    -c INPUT_FILE, --config=INPUT_FILE
                          Setting file to use gmail server
