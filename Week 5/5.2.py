# '''
# Problem 1: Count Unique Characters in a Script
# Approach: using a set, add the names of the characters to the set
# return the len of the set
# '''

# def count_unique_characters(script):
#     characters = set()
#     for element in script.keys():
#         if element not in characters:
#             characters.add(element)
#     return len(characters)

# script = {
#     "Alice": ["Hello there!", "How are you?"],
#     "Bob": ["Hi Alice!", "I'm good, thanks!"],
#     "Charlie": ["What's up?"]
# }
# print(count_unique_characters(script)) 

# script_with_redundant_keys = {
#     "Alice": ["Hello there!"],
#     "Alice": ["How are you?"],
#     "Bob": ["Hi Alice!"]
# }
# print(count_unique_characters(script_with_redundant_keys)) 

# '''
# Problem 2: Find Most Frequent Keywords
# Approach: keep a frequency of all of the keywords, and then find the max frequency, and then append the words that have that max frequency to the list that is then returned
# '''

# def find_most_frequent_keywords(scenes):
#     result = []
#     freq={}
#     for scene in scenes:
#         for act in scenes[scene]:
#             freq[act] = freq.get(act, 0) + 1
#     max_count = 0
#     for act, count in freq.items():
#         if count > max_count:
#             max_count = count
    
#     for act, count in freq.items():
#         if count == max_count:
#             result.append(act)
#     return result

# scenes = {
#     "Scene 1": ["action", "hero", "battle"],
#     "Scene 2": ["hero", "action", "quest"],
#     "Scene 3": ["battle", "strategy", "hero"],
#     "Scene 4": ["action", "strategy"]
# }
# print(find_most_frequent_keywords(scenes))

# scenes = {
#     "Scene A": ["love", "drama"],
#     "Scene B": ["drama", "love"],
#     "Scene C": ["comedy", "love"],
#     "Scene D": ["comedy", "drama"]
# }
# print(find_most_frequent_keywords(scenes)) 

# '''
# Problem 3: Track Scene Transitions
# Approach: using a deque, keep only two elements in the queue at once
# push opening into the queue
# size is 1, so push rising action into the queue
# form the string and print that string
# pop the first element out and then push the next element from scenes into the queue
# keep going until we have looped through every element in scenes

# better approach: instead of making sure there are only two elemets in the queue at once, push everything into the queue
# pop the first element, and then use a while loop while the queue is not empty, we have a variable that tracks the next element
# combine into a string and print it, and then have current be this next element so in the next iteration, we update the "next" element
# '''

# from collections import deque

# def track_scene_transitions(scenes):
#     if len(scenes) < 2:
#         print("")
#     queue = deque(scenes)
#     current = queue.popleft()

#     while queue:
#         next = queue.popleft()
#         print(f"Transition from {current} to {next}")
#         current=next

# scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
# track_scene_transitions(scenes)

# scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
# track_scene_transitions(scenes)

'''
Problem 4: Organize Scene Data by Date
Approach:
'''

def organize_scene_data_by_date(scene_records):
  pass

scene_records = [
    ("2024-08-15", "Climax"),
    ("2024-08-10", "Introduction"),
    ("2024-08-20", "Resolution"),
    ("2024-08-12", "Rising Action")
]
print(organize_scene_data_by_date(scene_records))

scene_records = [
    ("2023-07-05", "Opening"),
    ("2023-07-07", "Conflict"),
    ("2023-07-01", "Setup"),
    ("2023-07-10", "Climax")
]
print(organize_scene_data_by_date(scene_records))

