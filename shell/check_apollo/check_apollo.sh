#!/bin/bash

while true  
do
	see8080=`netstat -an | grep ":8080" | awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l`
	see8070=`netstat -an | grep ":8070" | awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l`
	see8090=`netstat -an | grep ":8090" | awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l`
	if [[ $see8080 -eq 0 || $see8070 -eq 0 || $see8090 -eq 0 ]]; then
		echo "listener port is down"
		echo "listener port is down">>~/apollo-quick/log/1.log
		cd ~/apollo-quick/
		./demo.sh stop
		./demo.sh start
	else
		echo "listener port is running"
		echo "端口正常" >>~/apollo-quick/log/1.log
	fi
   sleep 30  
done 
