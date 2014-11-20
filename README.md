speed_test
==========

配合 crontab 定時執行 speedtest_cli，並將結果（時間、ping、download、upload）寫入 CSV 供統計

### Requiremnet
* speedtest_cli

### usage
* crontab -e（每十五分鐘執行）

        */15 * * * * cd /Users/allenkuan/github/speed_test && /usr/local/bin/python /Users/allenkuan/github/speed_test/speedtest.py > /dev/null 2>&1
        
### result
* cat speedtest_log.csv

        "Thu Nov 20 13:15:40 2014", 68.204, 1.63, 2.14
        "Thu Nov 20 13:30:38 2014", 67.756, 1.44, 2.37