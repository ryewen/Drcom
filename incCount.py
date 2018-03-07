#!/usr/bin/enc python

file = "/root/count.txt"

f = open(file, 'r')
count = int(f.read())
f.close()

f = open(file, 'w')
f.write(str(count+1))
f.close()
