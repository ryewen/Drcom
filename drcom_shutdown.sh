#!/bin/sh

python="python"
drcompath="/usr/share/drcom/latest-wired.py"

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
		if [ "$word" = "$python" -o "$word" = "$drcompath" ]
		then
			equal=$(($equal+1))
		fi
		i=$(($i + 1))
	done
	if [ $equal -eq 2 ]
	then
		echo "kill $pid"
		kill -9 $pid
	fi	
done
