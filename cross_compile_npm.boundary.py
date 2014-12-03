#!/usr/bin/env python

import os
import sys
import subprocess

if len(sys.argv) < 2:
	print sys.argv[0] + " " + "<npm command>" + " " + "[node package module name]"
	sys.exit()

PATH_CROSS_COMPILER = "/opt/boundary/Toolchain/ARMEL/fsl-linaro-toolchain/bin"

print "adding cross compiler path"
PATH_OLD = os.environ['PATH']
print "old path = %(PATH_OLD)s"%locals()
PATH_NEW = PATH_OLD + ':' + PATH_CROSS_COMPILER
print "new path = %(PATH_NEW)s"%locals()
os.environ['PATH'] = PATH_NEW

os.environ['AR'] = "arm-fsl-linux-gnueabi-ar"
print "AR=" + os.environ['AR'] 
os.environ['CC'] = "arm-fsl-linux-gnueabi-gcc"
print "CC=" + os.environ['CC']
os.environ['CXX'] = "arm-fsl-linux-gnueabi-g++"
print "CXX=" + os.environ['CXX']
os.environ['LD'] = "arm-fsl-linux-gnueabi-g++ --sysroot=/opt/boundary/Sysroot/ARMEL/sysroot_armel"
print "LD=" + os.environ['LD']


print "============================================="
print "Cross Compiling Node Package Module"
print "============================================="
CMD_NPM = "npm"
CMD_NPM += " " + sys.argv[1]
CMD_NPM += " " + "--arch=arm"
CMD_NPM += " "

for arg in sys.argv[2:]:
	if arg != sys.argv[0]:
		CMD_NPM += arg + " "		

print CMD_NPM
subprocess.call(CMD_NPM, shell=True)

