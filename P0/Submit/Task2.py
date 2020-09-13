"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from datetime import datetime

#5 steps -> O(1)
phone_dict = {} 
phone_max = None
duration_max = 0
start_time = datetime.strptime("01-09-2016 00:00:00","%d-%m-%Y %H:%M:%S")
end_time = datetime.strptime("01-10-2016 00:00:00","%d-%m-%Y %H:%M:%S")  

#O(N)
for i in range(len(calls)):
    dt = datetime.strptime(calls[i][2],"%d-%m-%Y %H:%M:%S")
    if ((dt >= start_time) and (dt < end_time)):
        if calls[i][0] not in phone_dict:
            phone_dict[calls[i][0]] = int(calls[i][3])
        else: 
            phone_dict[calls[i][0]] += int(calls[i][3])
        if duration_max < phone_dict[calls[i][0]]:
            duration_max = phone_dict[calls[i][0]]
            phone_max = calls[i][0]
        if calls[i][1] not in phone_dict:
            phone_dict[calls[i][1]] = int(calls[i][3])
        else:
            phone_dict[calls[i][1]] += int(calls[i][3])
        if duration_max < phone_dict[calls[i][1]]:
            duration_max = phone_dict[calls[i][1]]
            phone_max = calls[i][1]

# O(1)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_max,duration_max))

# Overall: O(N)