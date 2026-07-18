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

'''
Problem 1: Array to Linked List
'''

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    if not arr:                        
        return None
    head = Node(arr[0])
    length = len(arr)
    current = head
    for i in range(1, length):          
        next_node = Node(arr[i])
        current.next = next_node
        current = next_node
    return head

mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))

'''
Problem 2: Get it out of here!
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

# Function with a bug!
def remove_by_value(head, val):
    if not head:
        return None
    if head.value == val:
        return head.next  

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  
            return head  
        current = current.next

    return head

head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))

print_linked_list(remove_by_value(head, "Waluigi"))

'''
Problem 3: Partition List Around Value
Approach: build two linked lists, one with value smaller than the threshold, and one with values larger than the threshold
then, link them together
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

def partition(head, val):
    less_dummy = Node(0)
    greater_dummy = Node(0)
    currentL = less_dummy
    currentG = greater_dummy

    current = head
    while current:
        if current.value < val:
            currentL.next = current
            currentL=currentL.next
        else:
            currentG.next = current
            currentG=currentG.next
        current=current.next
    
    currentG.next = None
    currentL.next = greater_dummy.next

    return less_dummy.next

head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(head, 3))

'''
Problem 4: Middle Match
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

def middle_match(head, val):
    fast = head
    slow = head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    if slow.value == val:
        return True
    else:
        return False

kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))
tournament_tracks = Node("Rainbow Road", Node("Bowser Castle", Node("Sherbet Land", Node("Yoshi Valley"))))

print(middle_match(kart_choices, "Wild Wing"))
print(middle_match(tournament_tracks, "Bowser Castle"))

'''
Problem 5: Put it in Reverse
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


def reverse(head):
    current = head
    previous = None
    while current:
        next_node = current.next
        current.next=previous
        previous=current
        current=next_node
    return previous

kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))

print_linked_list(reverse(kart_choices))

'''
Problem 6: Symmetrical
Approach: use the fast/slow pointer technique to find the middle of the linked list
then, reverse the second half of the linked list
then, go inward to check if each node is equal to each other
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

def is_symmetric(head):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    #now, slow is at the middle node. we now reverse the linked list
    previous=None
    current=slow
    while current:
        next_node = current.next
        current.next=previous
        previous=current
        current=next_node
    #now, the second half of the linked list has been reversed. now, iterate through both halves to check that the nodes are the same. current is pointing at the first node (last node) after reversal, and we get another pointer to start at the head of the linked list
    start=head
    while start and previous:
        if start.value != previous.value:
            return False
        start=start.next
        previous=previous.next
    return True

head1 = Node("Bitterling", Node("Crawfish", Node("Bitterling")))
head2 = Node("Bitterling", Node("Carp", Node("Koi")))

print(is_symmetric(head1))
print(is_symmetric(head2))