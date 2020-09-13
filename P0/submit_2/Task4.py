"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

people_set = set() # people answer calls, send texts and receive texts
call_set = set() 
telem_list = []

#O(N)
for i in range(len(texts)):
    people_set.add(texts[i][0])
    people_set.add(texts[i][1])

#O(N)
for i in range(len(calls)):
    people_set.add(calls[i][1])
    call_set.add(calls[i][0])

#O(N)    
for element in call_set:
    if element not in people_set:
        telem_list.append(element)
        
telem_list.sort() #O(NlogN)

print("These numbers could be telemarketers:")  
print(*telem_list, sep = "\n")

# Overall O(NlogN)