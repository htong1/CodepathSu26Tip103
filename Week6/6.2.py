'''
Problem 1: Greatest Node
'''

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

def find_max(head):
    maximum = 0  
    current = head
    while current:
        if current.value > maximum:
            maximum = current.value
        current=current.next
    return maximum
    
head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
#print(find_max(head2))

'''
Problem 2: Remove Tail
'''

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
# print_linked_list(remove_tail(head))

'''
Problem 3: Delete Duplicates in a Linked List
'''

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

def delete_dupes(head):
    counts = {}
    curr = head
    # tracking the frequency of each node value
    while curr:
        counts[curr.value] = counts.get(curr.value, 0) + 1
        curr = curr.next
        
    curr = head
    while curr.next:
        while counts[curr.next.value] > 1:
            curr.next = curr.next.next
        curr = curr.next
        
    return head 

# 1, 2, 3, 3, 4, 5
    

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))

'''
Problem 4: Does it Cycle
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

# print(has_cycle(peach))


peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))
# print(has_cycle(peach))

'''
Problem 5: Remove Nth Node from End of List
Approach: use the two pointer method
first move the fast pointer ahead by n steps
then, while fast.next exists, move both pointer by 1
when the loop exists, slow points to the node before the nth node from the end that we want to remove
we then do slow.next=slow.next.next
edge case: what if we need to remove the head?
we create a dummy head that points to the head, and so even if the head is removed, dummy always points to whatever the first node in the linked list is
'''

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

def remove_nth_from_end(head, n):
    dummy = Node("", head)
    fast = dummy
    slow = dummy
    #range is exclusive, and we want the fast pointer to advance n times
    for i in range(n+1):
        fast=fast.next
    while fast:
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return dummy.next

head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")

'''
Problem 6: Careful Reverse
'''

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
        
def reverse_first_k(head, k):
    previous = None
    current=head
    count = 0
    if not head: 
        return None
    while current and count < k:
        next_node = current.next
        current.next=previous
        previous=current
        current=next_node
        count+=1
    head.next=current
    return previous
        

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))