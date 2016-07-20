#!/usr/bin/env python

import os
import sys
import subprocess

if len(sys.argv) < 2:
	print sys.argv[0] + " " + "<npm command>" + " " + "[node package module name]"
	sys.exit()

PATH_CROSS_COMPILER = "/usr/local/oecore-i686/sysroots/i686-oesdk-linux/usr/bin/arm-oe-linux-gnueabi"

print "adding cross compiler path"
PATH_OLD = os.environ['PATH']
print "old path = %(PATH_OLD)s"%locals()
PATH_NEW = PATH_OLD + ':' + PATH_CROSS_COMPILER
print "new path = %(PATH_NEW)s"%locals()
os.environ['PATH'] = PATH_NEW

os.environ['AR'] = "arm-fsl-linux-gnueabi-ar"
print "AR=" + os.environ['AR']
os.environ['CC'] = "arm-oe-linux-gnueabi-gcc  -march=armv7-a -mthumb-interwork -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=/usr/local/oecore-i686/sysroots/cortexa9-vfp-neon-oe-linux-gnueabi "
print "CC=" + os.environ['CC']
os.environ['CXX'] = "arm-oe-linux-gnueabi-g++  -march=armv7-a -mthumb-interwork -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=/usr/local/oecore-i686/sysroots/cortexa9-vfp-neon-oe-linux-gnueabi "
print "CXX=" + os.environ['CXX']
os.environ['LINK'] = "arm-oe-linux-gnueabi-g++"
print "LINK=" + os.environ['LINK']
os.environ['STAGING_DIR'] = "/usr/local/oecore-i686/sysroots/cortexa9-vfp-neon-oe-linux-gnueabi"
print "STAGING_DIR=" + os.environ['STAGING_DIR']

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
