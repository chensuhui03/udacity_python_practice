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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_book = []  #O(1)

for i in range(len(texts)):   #2N -- O(N)
    phone_book.append(texts[i][0])
    phone_book.append(texts[i][1])
    
for i in range(len(calls)):  #2N -- O(N)
    phone_book.append(calls[i][0])
    phone_book.append(calls[i][1])
    
ct_phone_number = len(set(phone_book)) #N+1 -- O(N)

print("There are {} different telephone numbers in the records.".format(ct_phone_number)) #O(1)

# Overall O(N)

