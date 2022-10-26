#!/bin/bash
source /etc/profile
datadir=/home/pi

while true;
do
  count=`ps -ef | grep /home/pi/turnstile/app.py | grep -v grep|wc -l`
  if [ ${count} -eq 0 ]; 
  then

#启动进程
   
nohup python3 /home/pi/turnstile/app.py  > $datadir/log/turnstile.log &
  else
    echo "process is running"
  fi
  sleep 3
done
