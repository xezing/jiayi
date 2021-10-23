#!/bin/bash
source /etc/profile
logPath=/home/jiayi/xezing/N100_xu/log
cd /home/jiayi/xezing/N100_xu
mkdir -p log
for ((;;)); do
	currDate=`date -d today +"%Y%m%d"`
	logFile=${logPath}/gps_${currDate}.log
	devName=`dmesg | grep cp210x | tail -n 1 | awk '{if (index($0, "attached") > 0) {print $NF}}'`
	sudo chmod 777 /dev/${devName}
	sudo python2 gps_serial.py -d /dev/${devName} >> ${logFile} 2>&1
done
