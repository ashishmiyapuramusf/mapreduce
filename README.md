READme:

/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files Mapper.py,Reducer.py \
-input /user/cloudera/file.txt \
-output /user/cloudera/output \
-mapper "python Mapper.py" \
-reducer "python Reducer.py"
