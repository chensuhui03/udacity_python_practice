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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# PartA
b_answer_area = set() # Initiate a set of area codes (080) called. O(1)

# O(N)
for i in range(len(calls)):
    if not calls[i][0].startswith("(080)"):
        continue
    if calls[i][1].startswith("("): 
        # fixed lines
        idx = (calls[i][1].find(")"))+1
        b_answer_area.add(calls[i][1][:idx])
    elif calls[i][1].startswith("140"): 
        # telemarketer
        b_answer_area.add("140")
    else: 
        #mobile
        b_answer_area.add(calls[i][1][:4])
            
b_answer_area_list = list(b_answer_area) #O(N)
b_answer_area_list.sort() #O(N*logN)

print("The numbers called by people in Bangalore have codes:")
print(*b_answer_area_list, sep = "\n")

#Overall for Part A: O(NlogN)

# PartB:
b_call_ct = 0 # Initiate # of calls made by 080
b_answer_ct = 0 # Initiate # of calls answered by 080 and made by 080

for i in range(len(calls)):
    if calls[i][0].startswith("(080)"):
        b_call_ct += 1
        if calls[i][1].startswith("(080)"):
            b_answer_ct += 1
            
b_answer_percent = round(b_answer_ct/b_call_ct*100,2)

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(b_answer_percent))

# Overall for Part B: O(N)