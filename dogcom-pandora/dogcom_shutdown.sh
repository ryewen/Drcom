#!/bin/sh

cmd='/tmp/dogcom_pandora'

ps |while read str
do 
	#echo $str
	i=0
	pid=0
	equal=0
	for word in $str
	do
		if [ $i -eq 0 ]
		then
			pid=$word	
		fi
		if [ "$word" = "$cmd" ]
		then
			echo "kill $pid"
			kill -9 $pid
		fi
		i=$(($i + 1))
	done
done
