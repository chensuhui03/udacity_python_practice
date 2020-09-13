import hashlib
import datetime
import time

class Block:

    def __init__(self, timestamp, data, previous_hash=''):
        self.timestamp = timestamp
        if data == None:
            self.data = ''
        else:
            self.data = data    
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    
    def calc_hash(self):
    
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp)+str(self.data)+self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):

        return self.previous_hash + "|" + str(self.timestamp) + "|" + str(self.data)

class Blockchain:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data, timestamp = None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()
        if self.head is None:
            block = Block(timestamp, data)
            self.head = block
        else:
            previous_hash = self.tail.hash
            block = Block(timestamp, data, previous_hash)
            self.tail.next = block
        self.tail = block
        return
    
    def to_list(self):
        blocklist = list()
        block = self.head
        while block:
            blocklist.append(block)
            block = block.next
        return blocklist

# Test Case 1:
chain1 = Blockchain()
data1 = "A to B $10."
data2 = "B to C $5."
data3 = "C to A $5."
chain1.append(data1)
time.sleep(1)
chain1.append(data2)
time.sleep(1)
chain1.append(data3)
print(chain1.to_list())
# Expected result: 
# [|timestamp1|A to B $10., previoushash|timestamp2|B to C $5.,a_different_previous_hash|timestamp3|C to A $5.]

# Test Case 2:
chain2 = Blockchain()
data4 = ""
data5 = 1
chain2.append(data4)
chain2.append(data5)
print(chain2.to_list())
# [|timestamp1|, previoushash|timestamp2|1.]

# Test Case 3: 
chain3 = Blockchain()
chain3.append(None)
chain3.append(None)
print(chain3.to_list())
# [|timestamp1|, previoushash|timestamp2|]