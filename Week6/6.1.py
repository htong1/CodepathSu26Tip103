# # class Villager:
# #     def __init__(self, name, species, catchphrase):
# #         self.name = name
# #         self.species = species
# #         self.catchphrase = catchphrase
# #         self.furniture = []
	
# #     # "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree"
# #     def add_item(self, item_name):
# #         if item_name == "acoustic guitar" or item_name == "ronwood kitchenette" or item_name == "rattan armchair" or item_name == "kotatsu" or item_name == "cacao tree":
# #             self.furniture.append(item_name)
            
# # alice = Villager("Alice", "Koala", "guvnor")
# # print(alice.furniture)

# # alice.add_item("acoustic guitar")
# # print(alice.furniture)

# # alice.add_item("cacao tree")
# # print(alice.furniture)

# # alice.add_item("nintendo switch")
# # print(alice.furniture)

# from collections import deque

# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor
    
#      # "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree"
#     def add_item(self, item_name):
#         if item_name == "acoustic guitar" or item_name == "ronwood kitchenette" or item_name == "rattan armchair" or item_name == "kotatsu" or item_name == "cacao tree":
#             self.furniture.append(item_name)
	
# def of_personality_type(townies, personality_type):
#     return [townie.name for townie in townies if townie.personality == personality_type]

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))
	
# def message_received(start_villager, target_villager):
    
#     curr_villager = start_villager

#     while curr_villager.neighbor:
#         if curr_villager.neighbor == target_villager:
#             return True
        
#         curr_villager = curr_villager.neighbor
    
#     return False

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next

# # kk_slider = Node("K.K. Slider")
# # harriet = Node("Harriet")
# # saharah = Node("Saharah")
# # isabelle = Node("Isabelle")

# # # Add code here to link the above nodes
# # kk_slider.next = harriet
# # harriet.next=saharah
# # saharah.next=isabelle

# # print_linked_list(kk_slider)

# from collections import defaultdict

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def catch_fish(head):
#     if head:
#         print(f"I caught a {head.fish_name}")
#         head = head.next
#     else:
#         print("Aw, better luck next time!")
    
#     return head


# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

# # class Node:
# #     def __init__(self, fish_name, next=None):
# #         self.fish_name = fish_name
# #         self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.fish_name, end=" -> " if current.next else "\n")
# #         current = current.next

# def fish_chances(head, fish_name):
#     fish_freq = 0
#     total = 0
#     current = head
#     while current:
#         if current.fish_name == fish_name:
#             fish_freq += 1
#         total += 1
#         current = current.next
    
#     return round(fish_freq / total, 2)


# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def restock(head, new_fish):
#     to_add = Node(new_fish)
#     current = head
#     while current.next:
#         current=current.next
#     current.next = to_add
#     return head


# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print_linked_list(restock(fish_list, "Rainbow Trout"))