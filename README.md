# mapreduce
hdfs dfs –copyFromLocal somefile.txt /user/cloudersa/somefile.txt

/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-straeming.jar -files Mapper.py, Reduce.py -input /user/cloudera/test.txt -output /user/cloudera/output -mapper Mapper.py -reducer Reducer.py
