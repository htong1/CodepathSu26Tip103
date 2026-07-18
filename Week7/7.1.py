# Problem 3
import math

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

        
# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


        
def split_protein_chain(protein, k):
    temp = protein
    linked_length = 0
    segments = []
    
    while temp:
        linked_length += 1
        temp = temp.next
    # 8, 3 -> 8 % 3 = 2 
    #majority = math.ceil(linked_length / k)
    #minority = linked_length % k
    max_seg_length = math.ceil(linked_length / k)
    # max_seg_length = -(-linked_length // k)
    
    curr = protein
    count = 0
    temp = node = Node(0)
    
    while curr:
        node.next = curr
        curr = curr.next
        count += 1
        if count == max_seg_length:
            node.next = None
            segments.append(temp.next)
            count = 0
        elif curr.next == None:
            node.next = None
            segments.append(temp.next)
            count = 0
    return segments

protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)
    

# Problem 2 - Set A
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    slow = protein
    fast = protein
    result = []
    end_node = None
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break 
    end_node = slow
    current = slow.next
    while current != end_node:
        result.append(current.value)
        current=current.next
    result.append(current.value)
    return result
    
    

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))
"""






# Problem 1 - Set A
"""
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    head = dna_strand
    current = head
    temp_m = m
    temp_n = 0
    prev = None
    while current:
        if temp_n == 0:
            temp = current
            current = current.next
            temp_m -= 1
            if temp_m == 0:                     
                prev = temp
                prev.next = None
                temp_n = n
        else:
            current = current.next
            temp_n -= 1
            if temp_n == 0:
                prev.next = current
                temp_m = m
    return head
        

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))
"""