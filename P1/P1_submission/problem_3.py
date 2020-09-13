import sys
import heapq

class Node:
    
    def __init__(self,charactor,count,left=None,right=None):
        self.charactor = charactor
        self.count = count
        self.left = left
        self.right = right
    
    def get_charactor(self):
        return self.charactor
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def __lt__(self, other):
        return (self.count, self.charactor) < (other.count, other.charactor)

class Tree:
    def __init__(self, node = None):
        self.root = node
    
    def get_root(self):
        return self.root
        
def huffman_encoding(data):
    # counting word frequency
    word_count = counting(data)
    
    # creating a priority queue based on word_count using heapq
    word_heap = []
    for charactor, count in word_count.items():   
        node = Node(charactor,count)
        heapq.heappush(word_heap,node)
    
    # reconstructing the tree
    while len(word_heap) > 1:
        left_child = heapq.heappop(word_heap)
        right_child = heapq.heappop(word_heap)
        new_node = Node("",left_child.count+right_child.count,left_child,right_child)
        heapq.heappush(word_heap,new_node)
        
    huffman_tree = Tree(heapq.heappop(word_heap))
    
    # walk the tree to find code for each charactor and store in dict
    word_dict = walk_tree(huffman_tree)
    
    # based on the sentence, generate huffman code based on code table
    huffman_code = encode(data,word_dict)
    
    return huffman_code, huffman_tree


def counting(data):   
    word_count = dict()
    for i in range(len(data)):
        if data[i] not in word_count:
            word_count[data[i]] = 1
        else:
            word_count[data[i]] += 1
    return word_count


def walk_tree(tree):
    word_dict = dict()
    #walk the tree
    node = tree.get_root()
    code = []
    trav_tree_print_path(tree.get_root(),code,word_dict)
    return word_dict


def trav_tree_print_path(node,path,word_dict):
    if node is None:
        return 
    
    if not node.get_left_child() and not node.get_right_child():
        code = ''.join(path)
        word_dict[node.charactor] = code
    
    path.append("0")
    trav_tree_print_path(node.get_left_child(),path,word_dict)
    path.pop()
    path.append("1")
    trav_tree_print_path(node.get_right_child(),path,word_dict)
    path.pop()

    
def encode(data,word_dict):
    result = ""
    for i in range(len(data)):
        result += word_dict[data[i]]
    return result
    

def huffman_decoding(data,tree):
    decode = ""
    node = tree.get_root()
    for i in range(len(data)):
        if data[i] == "0":
            node = node.get_left_child()
        elif data[i] == "1":
            node = node.get_right_child()
        if node.charactor != "" and node.charactor is not None:
            decode += node.charactor
            node = tree.get_root()

    return decode                        


# Test Case
if __name__ == "__main__":
    codes = {}
    
    #Test Case 1:
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1110011011100101110101001100110010111111000001101110010000111110011001
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: The bird is the word


    #Test Case 2:
    a_normal_sequence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_normal_sequence)))
    # The size of the data is: 74
    print ("The content of the data is: {}\n".format(a_normal_sequence))
    # The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE

    encoded_data, tree = huffman_encoding(a_normal_sequence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 32
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 74
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE


    #Test Case 3:
    an_easy_pattern = "!bc!bc!bc"

    print ("The size of the data is: {}\n".format(sys.getsizeof(an_easy_pattern)))
    # The size of the data is: 58
    print ("The content of the data is: {}\n".format(an_easy_pattern))
    # The content of the data is: !bc!bc!bc

    encoded_data, tree = huffman_encoding(an_easy_pattern)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 28
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 101101011010110
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 58
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: !bc!bc!bc