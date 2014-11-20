#!/usr/bin/env python
# -*- coding: utf8 -*-
import subprocess
import re
import time

# 總是使用 2189 這台 speedtest server
# 2189) TFN Media Co., Ltd. (Kaohsiung, Taiwan) [15.05 km]
p = subprocess.Popen(["speedtest-cli", "--simple", "--server", "2189"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(out, err) = p.communicate()

pingResult = re.findall(r"Ping:\s(.*)\sms", out)
downloadResult = re.findall(r"Download:\s(.*)\sMbits/s", out)
uploadResult = re.findall(r"Upload:\s(.*)\sMbits/s", out)

currTime =  time.strftime("%c")

f = open('speedtest_log.csv', 'a+')
f.write('"%s", %s, %s, %s\n' % (currTime, pingResult[0], downloadResult[0], uploadResult[0]))
f.close()

print "Ping: %s ms, Download: %s Mbits/s, Upload %s Mbits/s" % (pingResult[0], downloadResult[0], uploadResult[0])