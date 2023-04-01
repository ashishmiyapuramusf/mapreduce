from operator import itemgetter
import sys
num = 0
num_temp = 0
count = 0
count_temp = 0

for line in sys.stdin:
        line = line.strip()
        num_temp, count_temp = line.split('\t',1)
        num_temp = int(num_temp)
        count_temp = int(count_temp)
        num = num + num_temp
        count = count + count_temp

print(num/count)
        

