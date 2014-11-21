speed_test
==========

配合 crontab 定時執行 speedtest_cli，並將結果（時間、Local IP Address、使用的 speedtest node、ping、download、upload）寫入 CSV 供統計

### Requiremnet
* speedtest_cli

### usage
* crontab -e（每十五分鐘執行）

        */15 * * * * cd /Users/allenkuan/github/speedtest2csv && /usr/local/bin/python /Users/allenkuan/github/speedtest2csv/speedtest2csv.py > /dev/null 2>&1
        
### result
* cat speedtest_20141120.csv

        Thu Nov 20 21:30:29 2014,220.133.45.30,Asia Pacific Telecom (Taipei),9.5,34.11,17.48
        Thu Nov 20 21:45:31 2014,220.133.45.30,Taiwan Fixed Network (Taipei),10.315,55.63,16.1
        Thu Nov 20 22:00:33 2014,220.133.45.30,Taiwan Fixed Network (Taipei),8.643,52.68,15.65
