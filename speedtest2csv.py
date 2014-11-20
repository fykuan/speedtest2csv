#!/usr/bin/env python
# -*- coding: utf8 -*-
import subprocess
import re
import time

# 總是使用 2189 這台 speedtest server
# 2189) TFN Media Co., Ltd. (Kaohsiung, Taiwan) [15.05 km]
p = subprocess.Popen(["/usr/local/bin/speedtest-cli"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(out, err) = p.communicate()

localIP = re.findall(r"Testing from.*?\((.*)\)...", out)
remoteHost = re.findall(r"by\s(.*)\s\[", out)
pingResult = re.findall(r"km.:\s(.*)\sms", out)
downloadResult = re.findall(r"Download:\s(.*)\sMbits/s", out)
uploadResult = re.findall(r"Upload:\s(.*)\sMbits/s", out)

currTime =  time.strftime("%c")
# 把 remoteHost 可能出現的逗號去掉
remoteHostStr = remoteHost[0].replace(",", "")

f = open('speedtest.csv', 'a+')
f.write('"%s",%s,%s,%s,%s,%s\r\n' % (currTime, localIP[0], remoteHostStr, pingResult[0], downloadResult[0], uploadResult[0]))
f.close()

print "Ping: %s ms, IP: %s, Remote Host: %s, Download: %s Mbits/s, Upload %s Mbits/s" % (pingResult[0], localIP[0], remoteHostStr, downloadResult[0], uploadResult[0])
