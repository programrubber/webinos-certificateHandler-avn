#!/usr/bin/env python

import os
import subprocess
from print_color import *

NODE_ADDON = "node_modules/certificate_manager.node"

subprocess.call(['sudo', 'apt-get', 'install', 'libssl-dev', 'libssl0.9.8', 'libgnome-keyring-dev']);
subprocess.call(['npm', 'install']);

if os.path.exists(NODE_ADDON) == False:
    printfail(os.getcwd() + "/" + NODE_ADDON + " doesn't exist")
