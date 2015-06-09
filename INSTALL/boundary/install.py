#!/usr/bin/env python

import os
import run_process
from print_color import *

NPM_CROSS_COMPILE = "cross_compile_npm.py"
NODE_ADDON = "node_modules/certificate_manager.node"

run_process.run_child_process(['./'+ NPM_CROSS_COMPILE, 'install']);

if os.path.exists(NODE_ADDON) == False:
    printfail(os.getcwd() + "/" + NODE_ADDON + " doesn't exist")
