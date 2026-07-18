# time complexity: O(n)
# space complexity: O(n)

def count_layers(sandwich):
    #base case
    if 1 == len(sandwich):
        return 1
    return 1 + count_layers(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))

def reverse_orders(orders):
    arr = orders.split(" ")
    
    return recursive_reverse(arr[1:]) + " " + arr[0]
    

def recursive_reverse(orderArray):
    if len(orderArray) == 1:
        return orderArray[0]
    
    return recursive_reverse(orderArray[1:]) + " " + orderArray[0]
    
print(reverse_orders("Bagel Sandwich Coffee"))

def can_split_coffee(coffee, n):
    if coffee == []:
        return True
    if coffee[0] % n != 0:
        return False
    return can_split_coffee(coffee[1:],n)
    

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))

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

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    temp = sandwich_a.next
    sandwich_a.next = merge_orders(sandwich_b, temp)
    
    return sandwich_a

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_d = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_d, sandwich_c))

def evaluate_ternary_expression_recursive(expression):
    stack = []
    def helper_itr(expression, index):
        if stack and stack[-1] == "?":
            stack.pop()                               
            true_exp = stack.pop()
            stack.pop()
            false_exp = stack.pop()
        
            if expression[-1] == "T":
                stack.append(true_exp)
            else:
                stack.append(false_exp)
        else:
            stack.append(expression[-1])