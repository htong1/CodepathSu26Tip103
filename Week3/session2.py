# '''
# Problem 1: Finding the Perfect Cruise
# '''

# def find_cruise_length(cruise_lengths, vacation_length):
#     low = 0
#     high = len(cruise_lengths)-1
#     while low<=high:
#         mid = (low+high)//2
#         if cruise_lengths[mid] == vacation_length:
#             return True
#         elif cruise_lengths[mid]<vacation_length:
#             low = mid+1
#         else:
#             high = mid-1
#     return False

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# '''
# Problem 2: Booking the Perfect Cruise Cabin
# Approach: two pointer technique using recursion
# for the iterative approach, we are using binary search, which has time complexity of O(logn)
# '''

# def find_cabin_index(cabins, preferred_deck, left=None, right=None):
#     if left is None:
#         left = 0
#     if right is None:
#         right=len(cabins)-1
#     if left > right:
#         return left
#     else:
#         mid = (left+right)//2
#         if cabins[mid] == preferred_deck:
#             return mid
#         elif cabins[mid] > preferred_deck:
#             right=mid-1
#             return find_cabin_index(cabins, preferred_deck, left, right)
#         else:
#             left=mid+1
#             return find_cabin_index(cabins, preferred_deck, left, right)

# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))

# '''
# Problem 3: Count Checked In Passengers
# '''

# def count_checked_in_passengers(rooms):
#     if rooms == []:
#         return 0
#     else:
#         if rooms[0] == 1:
#             return 1 + count_checked_in_passengers(rooms[1:])
#         else:
#             return count_checked_in_passengers(rooms[1:])

# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))

# '''
# Problem 4: Determining Profitability of Excursions
# Approach: start x at 0 and keep incrementing and check if at least x amount of elements in the list are greater than or equal to x?
# but that is a lot of redundant looping
# start x at 0, if it is satisfied, increment x, and keep incrementing until x is at its max possible value
# the only time you return -1 is when the list is all 0, because if you have an element that is 1 in the list, x=1 works
# '''

# def is_profitable(excursion_counts):
#     x=1
#     for i in range(len(excursion_counts)):
#         if excursion_counts[i] >= x:
#             x+=1
#     if x == 1 and len(excursion_counts)!=0:
#         return -1
#     else:
#         #count starts at 0, but we start checking when x=1
#         return x-1

# print(is_profitable([3, 5]))
# print(is_profitable([0, 0]))

# '''
# Problem 5: Finding the Shallowest Point
# Approach: using divide and conquer
#     Divide — split the problem into smaller subproblems
#     Conquer — solve each subproblem recursively
#     Combine — merge the solutions back together

# '''

# # def find_shallowest_point(depths):
# #     min_val = float('inf')
# #     for element in depths:
# #         if element < min_val:
# #             min_val = element
# #     return min_val

# #Divide and Conquer Approach

# def find_shallowest_point(depths):
#     #when using recursion to find the min, to break the problem down to its smallest case, when the list only has one element, that one element is the miniumum value
#     if len(depths) == 1:
#         return depths[0]
#     else:
#         #for the recursive case, I need to split the list into two halves
#         mid = len(depths)//2
#         left = depths[:mid]
#         right=depths[mid:]
#         #now need to write the recursive calls on each half to find the minimum of each
#         left_min = find_shallowest_point(left)
#         right_min = find_shallowest_point(right)
#         #now need to combine 
#         if left_min < right_min:
#             return left_min
#         else:
#             return right_min

#     return

# print(find_shallowest_point([5, 7, 2, 8, 3]))
# print(find_shallowest_point([12, 15, 10, 21]))

# #Time complexity: O(n)

# '''
# Problem 6: Cruise Ship Treasure Hunt
# Approach: to use the divide and conquer method, we start with the element in the top right corner
# if it is greater than treasure, it means the entire column is greater than treasure and we can remove that
# if it is less than treasure, that means the entire row is too small and we can remove that
# '''

# def find_treasure(matrix, treasure):
# 	row = 0
# 	col = len(matrix[0])-1
# 	while row<len(matrix) and col>=0:
# 		if matrix[row][col] == treasure:
# 			return (row, col)
# 		elif matrix[row][col] < treasure:
# 			row+=1
# 		elif matrix[row][col] > treasure:
# 			col-=1
# 	return (-1,-1)

# rooms = [
#     [1, 4, 7, 11],
#     [8, 9, 10, 20],
#     [11, 12, 17, 30],
#     [18, 21, 23, 40]
# ]

# print(find_treasure(rooms, 17))
# print(find_treasure(rooms, 5))


