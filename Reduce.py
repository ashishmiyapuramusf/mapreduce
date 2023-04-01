from operator import itemgetter
import sys
num = 0
num_temp = 0
count = 0
count_temp = 0


for line in sys.stdin:
        #Remove leading or trailing white spaces
        line = line.strip()
        #Parse the input
        num_temp, count_temp = line.split('\t',1)
        #Convert to int
        try:
            count_temp = int(count_temp)
            num_temp = int(num_temp)
        except ValueError:
            continue
        num = num + num_temp
        count = count + count_temp
#Calculate average
average = float(num) / float(count)
#Print average
print (average)
