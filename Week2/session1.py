# '''
# Problem 1: Counting Treasure
# Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.
# '''

# def total_treasures(treasure_map):
#     total = 0
#     for treasure in treasure_map.values():
#         total+=treasure
#     return total

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasures(treasure_map1))
# print(total_treasures(treasure_map2)) 

# '''
# Problem 2: Pirate Message Check
# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

# Approach: to solve this problem with a set, we build one set from the entire message and then check its size, since a set only contains unique elements
# so the size of the set must be 26
# '''

# def can_trust_message(message):
#     s=set()
#     for char in message:
#         if char.lower() >= 'a' and char.lower() <= 'z':
#             s.add(char.lower())
#     return len(s) == 26

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# '''
# Problem 3: Find All Duplicate Treasure Chests in an Array
# Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

# Approach: using a frequency map, count all of the frequencies and then use another loop to add only elements that have a frequency of 2 to the list
# '''

# def find_duplicate_chests(chests):
#     freq = {}
#     result = []
#     for element in chests:
#         if element not in freq:
#             freq[element] = 1
#         else:
#             freq[element] += 1
#     for element in freq:
#             if freq.get(element) == 2:
#                 result.append(element)
#     return sorted(result)

# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))

# '''
# Problem 4: Booby Trap
# Approach: use Counter to get a frequency map
# Then find the frequency of the frequencies
# if the length of that map is 1, then return true only if that frequency is 1, since only one letter removed will leave 0 characters
# if the length of that map is 2, it is true if the freqneucy of one of the characters is 1 or if the frequency of one of the characters is 1 more than the other character
# False otherwise
# '''
# from collections import Counter

# def can_make_balanced(code):
#     freq = Counter(code)
#     #take all the freqnencies as keys, then count the frquencies of those frequencies
#     freq_of_freq = Counter(freq.values())
#     #all characters share the same frequency
#     if len(freq_of_freq) == 1:
#         f = next(iter(freq_of_freq))
#         #is only true if the value is 1, meaning only one character exists or 
#         return f==1 or len(freq) == 1
    
#     if len(freq) == 2:
#         (f1, c1), (f2,c2) = sorted(freq_of_freq.items())
#         if f1 == 1 and c1 == 1:
#             return True
#         if f2 == f1+1 and c2 == 1:
#             return True
#     return False
    

# code1 = "arghh"
# code2 = "haha"

# print(can_make_balanced(code1)) 
# print(can_make_balanced(code2)) 

# '''
# Problem 5: Overflowing with Gold
# Approach: like sorted two sum using two pointers
# start with one pointer at the end, one at the front
# add and compare with target; if too smaller, increase front pointer
# if too big, decrease back pointer
# keep going until sum is equal to target
# '''

# def find_treasure_indices(gold_amounts, target):
#     ptr1 = 0
#     ptr2 = len(gold_amounts)-1
#     while gold_amounts[ptr1] + gold_amounts[ptr2] != target:
#         if gold_amounts[ptr1] + gold_amounts[ptr2] > target:
#             ptr2-=1
#         elif gold_amounts[ptr1] + gold_amounts[ptr2] < target:
#             ptr1+=1
#     return [ptr1, ptr2]

# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3))  

# # '''
# # Problem 6: Organize the Pirate Crew
# # Approach: 
# # '''

# def organize_pirate_crew(group_sizes):
#     if len(group_sizes) == 0:
#         return []
#     result = []
#     #group size is the key, list of pirates is the value
#     groups = {}
#     #iterate from 0 to n-1 to get all the pirates
#     for i in range(len(group_sizes)):
#         #if the group size is not in the map, then create a new key-value pair where the group size is the key and the list of key-size pirates
#         if group_sizes[i] not in groups:
#             groups[group_sizes[i]] = [i]
#             #if the group size is 1, I need to append it and then delete the group
#             if group_sizes[i] == 1:
#                 result.append(groups[group_sizes[i]])
#                 del groups[group_sizes[i]]
#         #if after adding the current pirate to its appropriate list, it fills up, we append the completed list to the result and delete the key-value pair so the next group with the same group size can be formed
#         elif len(groups[group_sizes[i]]) ==  group_sizes[i]-1:
#             # groups[group_sizes[i]] = groups[group_sizes[i]].append(i) -- no need to assign! assigning it will result in None
#             groups[group_sizes[i]].append(i)
#             result.append(groups[group_sizes[i]])
#             del groups[group_sizes[i]]
#         else:
#             #otherwise, just add the pirate to its appripriate group only
#             groups[group_sizes[i]].append(i)
#     return result


# group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
# group_sizes2 = [2, 1, 3, 3, 3, 2]

# print(organize_pirate_crew(group_sizes1))
# print(organize_pirate_crew(group_sizes2)) 


# '''
# Problem 7: Minimum Number of Steps to Match Treasure Maps
# Approach: only count the chars in 1 not in 2 and the excess, or deficit, but not both excess and deficit because you will overcount
# '''
# from collections import Counter

# def min_steps_to_match_maps(map1, map2):
#     freq1 = Counter(map1)
#     freq2 = Counter(map2)

#     count = 0

#     for key, value in freq1.items():
#         if key not in freq2:
#             count+=value
#         elif value > freq2[key]:
#             count+=(value-freq2[key])
#     return count

# map1_1 = "bab"
# map2_1 = "aba"
# map1_2 = "treasure"
# map2_2 = "huntgold"
# map1_3 = "anagram"
# map2_3 = "mangaar"

# print(min_steps_to_match_maps(map1_1, map2_1))
# print(min_steps_to_match_maps(map1_2, map2_2))
# print(min_steps_to_match_maps(map1_3, map2_3))


# '''
# Problem 8: Counting Pirates' Action Minutes
# Approach: basically, must loop through each list within logs
# count the number of unique minutes for each pirate
# after doing so, loop again and then put the number of pirates for each minute and return that list
# '''

# def counting_pirates_action_minutes(logs, k):
#     freq = {}
#     result = []
#     for i in range(1,k+1,1):
#         result.append(0)
#     for element in logs:
#         if element[0] not in freq:
#             s = set()
#             s.add(element[1])
#             freq[element[0]] = s
#         else:
#             freq[element[0]].add(element[1])
#     for element in freq.values():
#         result[len(element)-1]+=1
#     return result

# logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
# k1 = 5
# logs2 = [[1, 1], [2, 2], [2, 3]]
# k2 = 4

# print(counting_pirates_action_minutes(logs1, k1)) 
# print(counting_pirates_action_minutes(logs2, k2))

'''
# Problem 1: The Library of Alexandria
# Approach:
# '''

# def analyze_library(library_catalog, actual_distribution):
#     result = {}
#     for key, value in library_catalog.items():
#         if key in actual_distribution:
#             result[key] = actual_distribution[key] - value
#     return result


# library_catalog = {
#     "Room A": 150,
#     "Room B": 200,
#     "Room C": 250,
#     "Room D": 300
# }

# actual_distribution = {
#     "Room A": 150,
#     "Room B": 190,
#     "Room C": 260,
#     "Room D": 300
# }


# print(analyze_library(library_catalog, actual_distribution))

# '''
# Problem 2: Grecian Artifacts
# Approach:
# '''

# def find_common_artifacts(artifacts1, artifacts2):
#     art2= set(artifacts2)
#     result = []
#     for element in artifacts1:
#         if element in art2:
#             result.append(element)
#     return result

# artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
# artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

# print(find_common_artifacts(artifacts1, artifacts2))

'''
Problem 3: Souvenir Declutter
Approach:
'''

from collections import Counter
def declutter(souvenirs, threshold):
    result = []
    freq = Counter(souvenirs)
    for key,value in freq.items():
        if value < threshold:
            result.append(key)
    return result

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2

'''
Problem 4: Time Portals
Approach:
'''

def num_of_time_portals(portals, destination):
    

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))