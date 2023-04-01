#! /usr/bin/env python
import sys
for line in sys.stdin:
	line = line.strip()
	number = line.split()
	for i in number:
		print('%s\t%s' % (i,1))
	
