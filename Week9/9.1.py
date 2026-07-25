'''
Problem 1: Ivy Cutting
'''

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     if not root:
#         return []
#     result=[root]
#     node=root
#     while node.right:
#         result.append(node.right.val)
#         node=node.right
#     return result
     

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

'''
Problem 2: Ivy Cutting II
'''

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     if not root:
#         return []
#     return [root.val] + right_vine(root.right)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# '''
# Problem 3: Pruning Plans
# '''

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def survey_tree(root):
#     if not root:    
#         return []
#     return survey_tree(root.left) + survey_tree(root.right) + [root.val]

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# magnolia = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1"))
#                         TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))

# '''
# Problem 4: Sum Inventory
# '''

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def sum_inventory(inventory):
#     if not inventory:
#         return 0
#     return inventory.val+sum_inventory(inventory.left)+sum_inventory(inventory.right)

# """
#      40
#     /  \
#    5   10
#   /   /  \
# 20   1   30
# """

# inventory = TreeNode(40, 
#                     TreeNode(5, TreeNode(20)),
#                             TreeNode(10, TreeNode(1), TreeNode(30)))

# print(sum_inventory(inventory))

'''
Problem 5: Calculating Yield II
'''

'''

'''

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def get_most_specific(taxonomy):
#     result = []
#     def dfs(node):
#         if not node.left and not node.right:
#             result.append(node.val)
#             return
#         dfs(node.left)
#         dfs(node.right)

#     dfs(taxonomy)
#     return result

# """
#            Plantae
#           /       \
#          /         \
#         /           \ 
# Non-flowering     Flowering
#    /      \       /        \
# Mosses   Ferns Gymnosperms Angiosperms
#                              /     \
#                         Monocots  Dicots
# """
# plant_taxonomy = TreeNode("Plantae", 
#                           TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
#                                   TreeNode("Flowering", TreeNode("Gymnosperms"), 
#                                           TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

# print(get_most_specific(plant_taxonomy))

'''
Problem 7: Count Old Growth Trees
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0
    count=1 if root.val > threshold else 0
    return count+count_old_growth(root.left, threshold)+count_old_growth(root.right, threshold) 

"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))

#2 pointer string, hashmap problem, sweepline, matrix dfs, bfs, matrix simulation, lamp lights, sweepline
#seshuanna
#within 6 months you can only take it 3 times
#spam 
#trees and graphs
#muhammed ali, abduaziz, mathew