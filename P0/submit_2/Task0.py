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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2]))
# 3 steps O(1)

n = len(calls)-1 # 2 steps
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[n][0],calls[n][1],calls[n][2],calls[n][3]))
# 4 steps O(1)

# Overall O(1)




