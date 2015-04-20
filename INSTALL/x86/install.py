#!/usr/bin/env python

import subprocess

subprocess.call(['sudo', 'apt-get', 'install', 'libssl-dev', 'libssl0.9.8', 'libgnome-keyring-dev']);
subprocess.call(['npm', 'install']);
