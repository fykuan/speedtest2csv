#!/usr/bin/env python
# -*- coding: utf8 -*-
import re
import subprocess
import sys
import time

try:
    p = subprocess.Popen(["/usr/local/bin/speedtest-cli", "--server", "4505"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
    print "speedtest failed.."
    sys.exit(0)

(out, err) = p.communicate()
localIP = re.findall(r"Testing from.*?\((.*)\)...", out)
remoteHost = re.findall(r"by\s(.*)\s\[", out)
pingResult = re.findall(r"km.:\s(.*)\sms", out)
downloadResult = re.findall(r"Download:\s(.*)\sMbits/s", out)
uploadResult = re.findall(r"Upload:\s(.*)\sMbits/s", out)

currTime =  time.strftime("%c")

# 把 remoteHost 可能出現的逗號去掉
try:
    remoteHostStr = remoteHost[0].replace(",", "")
except Exception as e:
    print e

try:
    f = open('speedtest_%s.csv' % time.strftime("%Y%m%d"), 'a+')
    f.write('%s,%s,%s,%s,%s,%s\r\n' % (currTime, localIP[0], remoteHostStr, pingResult[0], downloadResult[0], uploadResult[0]))
    f.close()
    print "Ping: %s ms, IP: %s, Remote Host: %s, Download: %s Mbits/s, Upload %s Mbits/s" % (pingResult[0], localIP[0], remoteHostStr, downloadResult[0], uploadResult[0])
except:
    print "write log file failed.."
    sys.exit(0)

