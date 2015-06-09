#!/usr/bin/env python

import os
import sys

def set_node_path(cwd, platformName):
	nodePath = ""
	if platformName == "x86":
		nodePath = cwd + "/" + "INSTALL" + "/" + platformName + "/" + "node"	
	else:
		nodePath = cwd + "/" + "INSTALL" + "/" + platformName + "/" + "node-v0.10.20"
	os.environ['PATH'] = nodePath + ":" + os.environ['PATH']

def run_child_process(argvs):
	SHELL = "sh"
	EXE_STATEMENT = SHELL + ' -c ' + '"""' 
	for argv in argvs:
		EXE_STATEMENT = EXE_STATEMENT + argv + " "

	EXE_STATEMENT = EXE_STATEMENT + '"""' + ' &'

	os.system(EXE_STATEMENT)		

