#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files Mapper.py,Reduce.py -mapper 'python Mapper.py' -reducer 'python Reduce.py' -input /user/cloudera/file.txt -output /user/cloudera/outputassignment
