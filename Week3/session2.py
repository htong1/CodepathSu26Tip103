# from collections import deque

# def blueprint_approval(blueprints):
#     q = deque()
#     popped = []
#     q.append(blueprints[0])
    
#     for i in range(1, len(blueprints)):
#         last_element = q[-1]
#         first_element = q[0]     
        
#         if blueprints[i] > last_element:
#             q.append(blueprints[i])          
#         elif blueprints[i] < first_element:
#             q.appendleft(blueprints[i])     
#         else:
#             while blueprints[i] < last_element:
#                 popped.append(q.pop())
#                 last_element = q[-1]         
#             q.append(blueprints[i])
#             while popped:
#                 q.append(popped.pop())
    
#     return list(q)

# print(blueprint_approval([3, 5, 2, 1, 4])) #[1, 2, 3, 4, 5] q: [3], blueprints: 5, 2, 1, 4
# print(blueprint_approval([7, 4, 6, 2, 5])) #[2, 4, 5, 6, 7]

# def build_skyscrapers(floors):
#     count = 1
#     last = floors[0]
#     for i in range(1, len(floors)):
#         if floors[i] > last:
#             count += 1  
#         last = floors[i]
#     return count

# print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) #4
# print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  #4
# print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))  #2

# def max_corridor_area(segments):
#     max_area = 0
#     for i in range(len(segments)-1):
#         for j in range(i+1, len(segments)):
#             min_val = 0
#             if segments[i] < segments[j]:
#                 min_val = segments[i]
#             else:
#                 min_val = segments[j]
#             current_area = (j-i)*min_val
#             if current_area>max_area:
#                 max_area = current_area
#     return max_area


# print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) #49
# print(max_corridor_area([1, 1])) #1

'''
Problem 4: Dream Building Layout
'''
def min_swaps(s):
    min_val = float('inf')
    for element in s:
        if element < min_val:
            min_val = element
    return min_val

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  

