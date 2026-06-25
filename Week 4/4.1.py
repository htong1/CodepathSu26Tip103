

'''
You're tasked with filtering out brands that are not sustainable from a list of fashion brands. A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly materials, ethical labor practices, or being carbon-neutral.

Write the filter_sustainable_brands() function, which takes a list of brands and a criterion, then returns a list of brands that meet the criterion.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

'''
U: given a list of dictionaries, check to see if each brand contains the given criteria. if so, add to result list and then return the final list
M:
P:
I:
R:
E:

Time Complexity - O(n*k)
Space Complexity - O(n)
'''

# def filter_sustainable_brands(brands, criterion):
#     result = []
#     for brand in brands:
#         if criterion in set(brand['criteria']):
#             result.append(brand['name'])
#     return result


# brands = [
#     {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
#     {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
#     {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
#     {"name": "TrendyStyle", "criteria": ["trendy designs"]}
# ]

# brands_2 = [
#     {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
#     {"name": "FastStyle", "criteria": ["mass production"]},
#     {"name": "NatureWear", "criteria": ["eco-friendly"]},
#     {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
#     {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
#     {"name": "FastCloth", "criteria": ["cheap production"]}
# ]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))

'''
U: given a list of dictionaries, count the frequency of the given materials and return the dictionary
M
P
I
R
E
'''

'''
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))

Time Complexity: O(n*k)
Space Complexity: O(1
'''

# def count_material_usage(brands):
#     freq = {}
#     for element in brands:
#         for material in element["materials"]:
#             if material not in freq:
#                 freq[material] = 1
#             else:
#                 freq[material]+=1
#     return freq

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))

# def find_trending_materials(brands):
#     freq = {}
#     result = set()
#     for element in brands:
#         for material in element["materials"]:
#             if material not in freq:
#                 freq[material] = 1
#             else:
#                 freq[material]+=1

#             if freq[material] > 1:
#                 result.add(material)

            
#     return list(result)

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))


# def find_best_fabric_pair(fabrics, budget):
#     # fabrics.sort() # sort in-place
#     sortedFabrics = sorted(fabrics, key=lambda element: element[1]) # returns the sorted array
#     l, r = 0, len(sortedFabrics)-1
#     while l < r:
#         if sortedFabrics[l][1] + sortedFabrics[r][1] > budget:
#             r -= 1
#         else:
#             return [sortedFabrics[l][0], sortedFabrics[r][0]]
#     return []

# fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
# fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
# fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

# print(find_best_fabric_pair(fabrics, 45))
# print(find_best_fabric_pair(fabrics_2, 70))
# print(find_best_fabric_pair(fabrics_3, 60))

# def organize_fabrics(fabrics):
#     result = []
#     while fabrics:
#         result.append(fabrics.pop())
#     return [material for material, cost in sorted(result, key=lambda element: element[1], reverse = True)]



# fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
# fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
# fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

# print(organize_fabrics(fabrics))
# print(organize_fabrics(fabrics_2))
# print(organize_fabrics(fabrics_3))

# import heapq
# def process_supplies(supplies):
#     maxHeap = []
#     for material, priority in supplies:
#         heapq.heappush(maxHeap, (-priority, material))
#     res = []
#     while maxHeap:
#         priority, material = heapq.heappop(maxHeap)
#         res.append(material)
#     return res


# supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
# supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
# supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

# print(process_supplies(supplies))
# print(process_supplies(supplies_2))
# print(process_supplies(supplies_3))

# def calculate_fabric_waste(items, fabric_rolls):
#     print(fabric_rolls)
#     total = 0
#     for item, num in items:
#         total += num
    
#     return sum(fabric_rolls) - total
    

# items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
# fabric_rolls = [5, 5, 5]
# print(calculate_fabric_waste(items, fabric_rolls))

# items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
# fabric_rolls = [4, 4, 4]
# print(calculate_fabric_waste(items_2, fabric_rolls))

# items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
# fabric_rolls = [7, 5, 5]
# print(calculate_fabric_waste(items_3, fabric_rolls))

# '''
# Problem 8: Fabric Roll Organizer
# '''

# def organize_fabric_rolls(fabric_rolls):
#     sorted_rolls = sorted(fabric_rolls)
#     result = []
#     if len(sorted_rolls) % 2 == 0:
#         end=len(sorted_rolls)
#     else:
#         end=len(sorted_rolls)-1
#     for i in range(0, end, 2):
#         pair = (sorted_rolls[i], sorted_rolls[i+1])
#         result.append(pair)
#     if len(sorted_rolls) % 2 != 0:
#         result.append(sorted_rolls[len(sorted_rolls)-1])
#     return result

# fabric_rolls = [15, 10, 25, 30, 22]
# fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
# fabric_rolls_3 = [40, 10, 25, 15, 30]

# print(organize_fabric_rolls(fabric_rolls))
# print(organize_fabric_rolls(fabric_rolls_2))
# print(organize_fabric_rolls(fabric_rolls_3))

# '''
# Problem 1: Track Screen Time Usage
# Time Complexity: O(n)
# Space Complexity: O(n)
# '''

# def track_screen_time(logs):
#     freq={}
#     for (app, time) in logs:
#         if app not in freq:
#             freq[app] = time
#         else:
#             freq[app]+=time
#     return freq

# logs = [("Instagram", 30), ("YouTube", 20), ("Instagram", 25), ("Snapchat", 15), ("YouTube", 10)]
# logs_2 = [("Twitter", 10), ("Reddit", 20), ("Twitter", 15), ("Instagram", 35)]
# logs_3 = [("TikTok", 40), ("TikTok", 50), ("YouTube", 60), ("Snapchat", 25)]

# print(track_screen_time(logs))
# print(track_screen_time(logs_2))
# print(track_screen_time(logs_3))

# '''
# Problem 2: Identify Most Used Apps
# '''

# def most_used_app(screen_time):
#     max_time = 0
#     max_app = ""
#     for app, time in screen_time.items():
#         if time > max_time:
#             max_time = time
#             max_app = app
#     return max_app

# screen_time = {"Instagram": 55, "YouTube": 30, "Snapchat": 15}
# screen_time_2 = {"Twitter": 25, "Reddit": 20, "Instagram": 35}
# screen_time_3 = {"TikTok": 90, "YouTube": 90, "Snapchat": 25}

# print(most_used_app(screen_time))
# print(most_used_app(screen_time_2))
# print(most_used_app(screen_time_3))

# '''
# Problem 3: Weekly App Usage
# '''

# def most_varied_app(app_usage):
#     max_diff = 0
#     max_diff_app = ""
#     for app, times in app_usage.items():
#         curr_diff = max(times) - min(times)
#         if curr_diff>max_diff:
#             max_diff = curr_diff
#             max_diff_app=app
#     return max_diff_app

# app_usage = {
#     "Instagram": [60, 55, 65, 60, 70, 55, 60],
#     "YouTube": [100, 120, 110, 100, 115, 105, 120],
#     "Snapchat": [30, 35, 25, 30, 40, 35, 30]
# }

# app_usage_2 = {
#     "Twitter": [15, 15, 15, 15, 15, 15, 15],
#     "Reddit": [45, 50, 55, 50, 45, 50, 55],
#     "Facebook": [80, 85, 80, 85, 80, 85, 80]
# }

# app_usage_3 = {
#     "TikTok": [80, 100, 90, 85, 95, 105, 90],
#     "Spotify": [40, 45, 50, 45, 40, 45, 50],
#     "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
# }

# print(most_varied_app(app_usage))
# print(most_varied_app(app_usage_2))
# print(most_varied_app(app_usage_3))

# '''
# Problem 4: Daily App Usage Peaks
# '''

# def peak_usage_hours(screen_time):
#     peak_time = 0
#     max_time = 0
#     peak_sum = 0
#     for i in range(0, len(screen_time)-2):
#         curr_sum = screen_time[i] + screen_time[i+1] + screen_time[i+2]
#         if curr_sum>max_time:
#             peak_time = i
#             peak_sum = curr_sum
#     return (peak_time, peak_sum)

# screen_time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
# screen_time_2 = [5, 15, 10, 20, 30, 25, 50, 40, 35, 45, 60, 55, 65, 75, 70, 85, 95, 90, 100, 110, 105, 115, 120, 125]
# screen_time_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# print(peak_usage_hours(screen_time))
# print(peak_usage_hours(screen_time_2))    
# print(peak_usage_hours(screen_time_3)) 

# '''
# Problem 5: App Usage Pattern Recognition
# Approach: create every possible subarray (each subarray is a pattern)
# for each subarray, count how many times it appears
# return the one that has the greatest frequency

# problem: cannot use a dictionary with lists as keys because lists are mutable, and for dictionaries, we cannot use lists as keys because they are miutable and thus not hashable
# instead, we use tuples as the key in the dictionary
# '''

# '''
# Start from length 1, and check to see if the next element of length 1 is the same as this one
# if so, increment count
# and keep going until the pattern breaks
# need to check every element at every index and every pattern of every length, and keep a count of the current pattern length, and current repetition count
# if the current pattern is longer than the previous pattern that was saved as the best one, and the current pattern repeats, this longer pattern becomes the better one
# only if the best_pattern and the current pattern have the same length do we 
# '''
# def find_longest_repeating_pattern(app_logs):
#     best_pattern = None
#     best_count = 0
#     n=len(app_logs)

#     for length in range(1, n//2+1):
#         for i in range(n-length):
#             count = 1
#             j = i + length
#             while j + length<=n:
#                 current_chunk = app_logs[i: i+length]
#                 next_chunk = app_logs[j: j+length]
#                 if current_chunk == next_chunk:
#                     count+=1
#                     j+=length
#                 else:
#                     break
#             if best_pattern is None:
#                 current_best_length=0
#             else:
#                 current_best_length=len(best_pattern)
#             if count>=2 and length>current_best_length:
#                 best_pattern = app_logs[i:i+length]
#                 best_count=count
#     return best_pattern, best_count

# # wrong approach, as we assumed the problem was asking the longest pattern that repeats anywhere, and not necessarily consecutively
# # def find_longest_repeating_pattern(app_logs):
# #     n = len(app_logs)
# #     best_pattern = None
# #     best_count = 0

# #     # length of each subarray/pattern
# #     # we divide by 2 because the pattern should repeat at least twice
# #     for length in range(1, n//2+1):
# #         # we reset after every iteration because we are counting patterns of a certain length everytime, and keeping the pattern with the longest repetition
# #         freq={}

# #         # this is the start of each pattern subarray throughout the list
# #         # here, we are employing the sliding window technique where the window size is of len length across the entire array
# #         for i in range(n-length+1):
# #             # we take the current window and create a tuple out of it
# #             pattern=tuple(app_logs[i:i+length])
# #             # count how many times this pattern has appeared so far
# #             freq[pattern] = freq.get(pattern, 0)+1
        
# #         # check if any pattern of this length repeats
# #         for pattern, count in freq.items():
# #             #here, count is the number of times the pattern repeats
# #             #we want to check that if the length of the current pattern is better than the best pattern and the count is greater than the current best count
# #             #len(best_pattern)[current_best_length] > len(pattern), best_count>count 
# #             if best_pattern is None:
# #                 current_best_length = 0
# #                 best_pattern=pattern
# #             else:
# #                 current_best_length = len(best_pattern)
# #                 best_pattern=pattern
# #             if count>best_count and current_best_length<len(pattern):
# #                 best_count=count
# #                 best_pattern = pattern
# #     return best_pattern, best_count




# app_logs = ["Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Facebook", "Twitter", "Instagram"]
# app_logs_2 = ["Facebook", "Instagram", "Facebook", "Instagram", "Facebook", "Instagram", "Snapchat", "Snapchat", "Snapchat", "Instagram"]
# app_logs_3 = ["WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook", "WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook"]

# print(find_longest_repeating_pattern(app_logs))
# print(find_longest_repeating_pattern(app_logs_2))
# print(find_longest_repeating_pattern(app_logs_3))

# '''
# Problem 6: Screen Time Session Management
# use a stack, push onto the stack everytime there is an open, and pop off of the stack when there is a close
# Time Complexity: O(nxm) -- the use of .split takes linear time, and n is linear for going through the actions list
# Space Complexity: O(n) -- created a stack that could grow up to O(n) size where there are only open operations and we keep pushing n elements from actions to the stack
# '''

# def manage_screen_time_sessions(actions):
#     status = []
#     for element in actions:
#         words = element.split(" ")
#         operation = words[0]
#         if operation == "OPEN":
#             status.append(words[1])
#         elif operation == "CLOSE":
#             if status == []:
#                 return False
#             else:
#                 top = status[-1]
#                 if top != words[1]:
#                     return False
#                 status.pop()
#     return True
        

# actions = ["OPEN Instagram", "OPEN Facebook", "CLOSE Facebook", "CLOSE Instagram"]
# actions_2 = ["OPEN Instagram", "CLOSE Instagram", "CLOSE Facebook"]
# actions_3 = ["OPEN Instagram", "OPEN Facebook", "CLOSE Instagram", "CLOSE Facebook"]

# print(manage_screen_time_sessions(actions))  
# print(manage_screen_time_sessions(actions_2))  
# print(manage_screen_time_sessions(actions_3)) 

# '''
# Problem 7: Digital Wellbeing Dashboard Analysis
# Accessing nested map fields:
# weekly_usage = {
#     "Monday": {"Social Media": 120, "Entertainment": 60, "Productivity": 90},
#     "Tuesday": {"Social Media": 100, "Entertainment": 80, "Productivity": 70},
#     ...
# }
# outer layer:  day name → inner dict
# inner layer:  category name → minutes

# # outer layer — get one day
# weekly_usage["Monday"]
# → {"Social Media": 120, "Entertainment": 60, "Productivity": 90}

# # inner layer — get one category from one day
# weekly_usage["Monday"]["Social Media"]
# → 120

# '''

# def analyze_weekly_usage(weekly_usage):
#     freq = {}
#     max_day_count = 0
#     busiest_day = None
#     #looping through a map like this makes every week variable represent the key
#     # for week in weekly_usage:
#     #     freq["Social Media"] = freq.get("Social Media", 0)+weekly_usage[week]["Entertainment"]
#     #     freq["Entertainment"] = freq.get("Entertainment", 0)+weekly_usage[week]["Entertainment"]
#     #     freq["Productivity"] = freq.get("Productivity", 0)+weekly_usage[week]["Productivity"]
#     for day in weekly_usage:
#         for category, minutes in weekly_usage[day].items():
#             freq[category] = freq.get(category, 0)+minutes
#         day_total = sum(weekly_usage[day].values())
#         if day_total > max_day_count:
#             max_day_count = day_total
#             busiest_day = day
#     max_cat = max(freq, key=lambda cat: freq[cat])
#     result = {}
#     result["total_category_usage"] = freq
#     result["busiest_day"] = day
#     result["most_used_category"] = max_cat
#     return result 

# weekly_usage = {
#     "Monday": {"Social Media": 120, "Entertainment": 60, "Productivity": 90},
#     "Tuesday": {"Social Media": 100, "Entertainment": 80, "Productivity": 70},
#     "Wednesday": {"Social Media": 130, "Entertainment": 70, "Productivity": 60},
#     "Thursday": {"Social Media": 90, "Entertainment": 60, "Productivity": 80},
#     "Friday": {"Social Media": 110, "Entertainment": 100, "Productivity": 50},
#     "Saturday": {"Social Media": 180, "Entertainment": 120, "Productivity": 40},
#     "Sunday": {"Social Media": 160, "Entertainment": 140, "Productivity": 30}
# }

# print(analyze_weekly_usage(weekly_usage))

# '''
# Problem 8: Optimizing Break Times
# '''

# def find_best_break_pair(break_times, target):
#     if len(break_times)<2:
#         return ()
#     sorted_times = sorted(break_times)
#     l, r = 0, len(break_times)-1
#     rl, rr = 0, len(break_times)-1
#     best_sum_diff = float('inf') # used to keep track of how close the sum is to the target value
#     best_val_diff = float('inf') # used in case of a tie, when there are two sets of indices that add up to target or the same, and thus we must check to see that the difference between the two values is the smallest
#     while l<r:
#         current_sum = sorted_times[l] + sorted_times[r]
#         sum_diff = abs(current_sum-target)
#         val_diff = abs(sorted_times[l]-sorted_times[r])
#         if sum_diff < best_sum_diff:
#             best_sum_diff = sum_diff
#             rl, rr = l,r
#         elif sum_diff == best_sum_diff and val_diff < best_val_diff:
#             best_val_diff = val_diff
#             rl, rr = l, r
#         if current_sum > target:
#             r-=1
#         elif current_sum < target:
#             l+=1
#         else:
#             l+=1
#     return (sorted_times[rl], sorted_times[rr])

# break_times = [10, 20, 35, 40, 50]
# break_times_2 = [5, 10, 25, 30, 45]
# break_times_3 = [15, 25, 35, 45]
# break_times_4 = [30]

# print(find_best_break_pair(break_times, 60))  
# print(find_best_break_pair(break_times_2, 50))  
# print(find_best_break_pair(break_times_3, 70))  
# print(find_best_break_pair(break_times_4, 60))  