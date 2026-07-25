from collections import deque 

# # Tree Node class
# class TreeNode:
#     def __init__(self, key, val, left=None, right=None):
#         self.key = key      # Plant rarity
#         self.val = val      # Plant name
#         self.left = left
#         self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

'''
Problem 1: Sorting Plants by Rarity
use dfs here; inorder traversal is a traversal order for dfs
how to know we need to use dfs for this problem: full traversal, inorder traversal is specific to dfs
when a problem says to use inorder, preorder, postorder, its dfs
DFS (depth-first, uses recursion/stack):
  - inorder/preorder/postorder traversals
  - "explore all the way down a path" problems
  - tree height, path sums, "does a path exist"
  - anything needing the recursive structure (subtree results)

BFS (breadth-first, uses a queue):
  - level-by-level processing ("level order traversal")
  - shortest path in unweighted graphs
  - "closest" or "minimum steps" problems
'''


# def sort_plants(collection):
#     result=[]
#     def dfs(node):
#         if not node:
#             return ()
#         dfs(node.left)
#         result.append((node.val, node.key))
#         dfs(node.right)
#     dfs(collection)
#     return result

# """
#          (3, "Monstera")
#         /               \
#    (1, "Pothos")     (5, "Witchcraft Orchid")
#         \                 /
#   (2, "Spider Plant")   (4, "Hoya Motoskei")
# """

# # Using build_tree() function at the top of page
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

'''
Problem 2: Flower Finding
Approach: here, we need to go through every node in the tree to see if a specific element can be found, so we can use bfs or dfs
Try dfs first, then I need to learn how to implement bfs with deque
or, I dont even have to use dfs or bfs, just recursion
'''

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

# def find_flower(inventory, name):
#     def dfs(node):
#         if not node:
#             return False
#         if node.val == name:
#             return True
#         return dfs(node.left) or dfs(node.right)
#     return dfs(inventory)



# """
#          Rose
#         /    \
#       Lilac   Tulip
#      /  \       \
#   Daisy  Lily  Violet
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
# garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

'''
Problem 3: Adding a New Plant to the Collection
Approach: for this problem, we do not need to use dfs
because it is a binary search tree, at each node, we decide if we need to go left or right by comparison
if name < node.val --> go left
if name >= node.val --> go right

why we do collection.left = add_plant()
When the child is None, the recursive call creates a new node and returns it. Something has to catch that new node and link it to the tree. That's what the assignment does — collection.left = grabs the newly created node and attaches it as the left child.
'''

# def add_plant(collection, name):
#     if not collection:
#         return TreeNode(name)
#     if name < collection.val:
#         collection.left = add_plant(collection.left, name)
#     else:
#         collection.right = add_plant(collection.right, name)

#     return collection

# """
#             Money Tree
#         /              \
# Fiddle Leaf Fig    Snake Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))

'''
Problem 4: Remove Plant
Approach: when we remove a node from a binary search tree, there are two cases:
    if the removed node has two children, there are three steps to replacing inorder:
        find the predecessor of pilea
        copy the predecessor's value into the removed node
        delete the original removed node from the left subtree
    if the removed node is a leaf node, just remove
    if the removed node has no left child, we append the right child to the mot recent node in the right subtree on its right side

    still, we want to traverse through the BST, and only go to subtrees we need to go to depending on whether the name is < or >, alphabetically
'''

# def remove_plant(collection, name):
#     if not collection:
#         return None
#     if name < collection.val:
#         collection.left = remove_plant(collection.left, name)
#     elif name > collection.val:
#         collection.right = remove_plant(collection.right, name)
#     else:
#         #three cases when finding the node:
#         #case 1, its a leaf node, so we just remove it
#         if not collection.right and not collection.left:
#             return None
#         #case 2: only one child, replace the removed node with the child
#         if not collection.right:
#             return collection.left
#         if not collection.left:
#             return collection.right
#         else:
#             pred=collection.left
#             while pred.right:
#                 pred=pred.right
#             collection.val = pred.val
#             collection.left=remove_plant(collection.left, pred.val)

# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#               \        /   \
#              Ivy    Orchid  ZZ Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(remove_plant(collection, "Pilea"))

'''
Problem 5: Find Most Common Plants in Collection
Approach: 
    inorder traversal the tree and convert itinto a flat sorted list, since for BST, using inorder traversal puts the same elements in consecutive order (use dfs for this part)
    then traverse the list and find the max count values like normal
'''

# def find_most_common(root):
#     values = []
#     def dfs(node):
#         if not node:
#             return
#         dfs(node.left)
#         values.append(node.val)
#         dfs(node.right)
#     dfs(root)

#     if not values:
#         return []
#     max_count = 0
#     max_vals = []
#     current_val = None
#     current_count = 0

#     for element in values:
#         if element == current_val:
#             current_count+=1
#         else:
#             current_val = element
#             current_count=1

#         if current_count > max_count:
#             max_count=current_count
#             max_vals = [current_val]
#         elif current_count == max_count:
#             max_vals.append(current_val)
#     return max_vals

# """
#     Hoya
#       \ 
#       Pothos
#       /
#     Pothos
# """

# # Using build_tree() function at top of page
# values = ["Hoya", None, "Pothos", "Pothos"]
# collection1 = build_tree(values)

# """
#       Hoya
#     /      \ 
#   Aloe    Pothos
#   /        /
#  Aloe   Pothos
# """
# values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
# collection2 = build_tree(values)

# print(find_most_common(collection1))
# print(find_most_common(collection2))

'''
Problem 6: Split Collection
Approach: for this problem, find the target node, and then all nodes in the left subtree is less than it, and all other nodes are greater?
recursive split:
    case 1: if root.val <= target, the root's entire left subtree is smaller, but the right subtree might have values <= target, so must split the right subtree too
    case 2: if root.val > target, all nodes in its right subtree is larger, but the left subtree
'''

'''
explanation:
    the fuction split_collection returns a pair of values: the small tree and the large tree
    if the node is empty, there is nothing to split, so the function returns two empty trees
    when node.val<=target, this node belongs in the smaller tree
        its left child is even smaller, so the entire left subtree belongs in small. so we dont touch it, it stays attached
        but the right subtree could have values on both sides of target, so we split the right subtree
'''
# def split_collection(node, target):
#     if not node:
#         return [None, None]
#     if node.val <= target:
#         #this line already splits the right subtree so that the node.right only has nodes <= target when called recursively
#         small, large = split_collection(node.right, target)   # recurse ONE side
#         #we then set the remaining smaller nodes to small
#         node.right = small
#         #we return node, large because node represents the small subtree, whereas large from the recursive call gets all the bigger nodes
#         return [node, large]
#     else:
#         #same logic, just opposite
#         small, large = split_collection(node.left, target)    # recurse ONE side
#         node.left = large
#         return [small, node]


# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#            /   \        /   \
#         Aloe   Ivy    Orchid  ZZ Plant
# """

# # Using build_tree() function at the top of the page
# values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of the page
# left, right = split_collection(collection, "Hoya")
# print_tree(left)
# print_tree(right)

# '''
# Problem 7: Pruning Pothos
# Approach: use dfs to get to all of the leaf nodes, and then once at leaf node, if it has no children and its val is target, remmove it
#     need to recurse back up though to see if the parent becomes a leaf node and must be removed
#     for dfs, need to use postorder traversal, where you visit the right node, left node, and then the parent node
#     we want to visit the parent node last because we need to recurse on the parent node to see if it needs to be removed too
# '''

# def prune(root, target):
#     def dfs(node):
#         if not node:
#             return None
#         node.left=dfs(node.left)
#         node.right=dfs(node.right)

#         if node.val == target and not node.left and not node.right:
#             return None
        
#         return node
#     return dfs(root)
# """
#          Healthy
#         /       \
#      Dying    Healthy
#      /          /  \
#    Dying     Dying  New Growth
# """

# # Using build_tree() function at the top of the page
# values = ["Healthy", "Dying", "Healthy", "Dying", None, "Dying", "New Growth"]
# pothos1 = build_tree(values)

# # Using print_tree() function at the top of the page
# print_tree(prune(pothos1, "Dying"))

class TreeNode():
    def __init__(self, species, parent=None, left=None, right=None):
        self.val = species
        self.parent = parent # Parent of node
        self.left = left
        self.right = right

'''
Problem 8: Find the Lowest Common Ancestor in a Plant Tree Based on Species Name
Approach:
    I think for this problem, also use dfs and postorder traversal
    we go to each subtree, find the two children, and then recurse up to see which parent is common to both of them

right approach:
    since each child has reference to its parent, this is basically a linked list problem where we can find two linked lists, each starting from p and q, and then put all nodes of one in a set and check for each node in the other, if its in the set
    return the first node that is in the set
    but because we are given p and q as strings, we need to find the ndoes for p and q first
'''

def lca(root, p, q):
    if not root:
        return None
    current=root
    p_node=None
    q_node=None
    while current:
        if current.val == p:
            p_node = current
            break
        elif current.val > p:
            current=current.left
        else:
            current=current.right
    current=root
    while current:
        if current.val == q:
            q_node = current
            break
        elif current.val > q:
            current=current.left
        else:
            current=current.right
    ancestors = set()

    while p_node:
        ancestors.add(p_node)
        p_node=p_node.parent

    while q_node:
        if q_node in ancestors:
            return q_node.val
        q_node=q_node.parent
    return None

"""
          fern
        /      \
       /        \
  cactus        rose
   /  \         /   \
bamboo dahlia lily  oak
"""
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

print(lca(fern, "cactus", "rose"))
print(lca(fern, "bamboo", "oak"))