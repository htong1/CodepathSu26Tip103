# '''
# Problem 1: Find Millenium Falcon Part I
# Time Complexity: O(logn) if the array is already sorted, which makes binary search faster than linear search
# but if it wasnt sorted, to use binary sort, you would have to sort first, making the total time complexity O(nlogn)
# Space Complexity: O(1)
# '''

# def check_stock(inventory, part_id):
#     left = 0
#     right = len(inventory)-1
#     while left<=right:
#         middle = left+(right-left)//2
#         if inventory[middle] > part_id:
#             right=middle-1
#         elif inventory[middle] < part_id:
#             left=middle+1
#         else:
#             return True
#     return False
        

# print(check_stock([1, 2, 5, 12, 20], 20))
# print(check_stock([1, 2, 5, 12, 20], 100))

# '''
# Problem 2: Find Millenium Falcon Part II--Recursion with Binary Search
# to do binary search recursively, we need to use a helper function. the reason we need to use a helper function is because we need to change the function signature to return additional information everytime
# for binary search, we need to return the left and right positions after every half
# '''

# def check_stock(inventory, part_id):
#     return helper(inventory, part_id, 0, len(inventory)-1)

# def helper(arr, target, left, right):
#     if left > right:
#         return False
#     mid = left + (right-left)//2
#     if arr[mid] == target:
#         return True
#     elif arr[mid]>target:
#         return helper(arr, target, left, mid-1)
#     else:
#         return helper(arr, target, mid+1, right)
    
# '''
# nested helper version (cleaner, because you only have to pass left and right as the parameters):
# def search(arr, target):
#     def helper(left, right):
#         if left > right:
#             return False
#         mid = left + (right - left) // 2
#         if arr[mid] == target:      # arr and target visible via closure!
#             return True
#         elif arr[mid] > target:
#             return helper(left, mid - 1)   # only pass what CHANGES
#         else:
#             return helper(mid + 1, right)
    
#     return helper(0, len(arr)-1)
# '''


# print(check_stock([1, 2, 5, 12, 20], 20))
# print(check_stock([1, 2, 5, 12, 20], 100))

# '''
# Problem 3: Find First and Last Frequency Positions
# Approach: do binary search twice, where if I find the target, I search the left half only and then the right half only
# to do this iteratively, we would need two while loops each doing binary search, but in their own direction
# so the overall time complexity is still O(logn)
# '''

# def find_frequency_positions(transmissions, target_code):
#     left, right = 0, len(transmissions)-1
#     first = -1
#     #searching left
#     while left<=right:
#         mid=left+(right-left)//2
#         if transmissions[mid]==target_code:
#             first=mid
#             right = mid-1
#         elif transmissions[mid] < target_code:
#             left = mid+1
#         else:
#             right=mid-1
    
#     if first == -1:
#         return (-1,-1)
    
#     #searching right
#     left, right = 0, len(transmissions)-1
#     last = -1
#     while left<=right:
#         mid=left+(right-left)//2
#         if transmissions[mid]==target_code:
#             last = mid
#             left=mid+1
#         elif transmissions[mid] < target_code:
#             left=mid+1
#         else:
#             right=mid-1
#     return (first, last)


# print(find_frequency_positions([5,7,7,8,8,10], 8))
# print(find_frequency_positions([5,7,7,8,8,10], 6))
# print(find_frequency_positions([], 0))

# '''
# Problem 4: Smallest Letter Greater Than Target
# Approach: we need to find the letter immediately after the target, and we can use binary search to do this
# instead of having a condition in the binary search that terminates when we find the target, we can bias the search to find the boundary between the target and its immediate right neighbor
# so if the mid value is <= target, we search right
# if the mid value is greater, we search left
# when the while loop exits, the left pointer points to the first index where the letter is larger than target
# '''

# def next_greatest_letter(letters, target):
#     left, right = 0, len(letters)-1
#     while left<=right:
#         mid = left+(right-left)//2
#         if letters[mid] <= target:
#             left=mid+1
#         else:
#             right=mid-1
#     if left>=len(letters):
#         return letters[0]
#     return letters[left]

# letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

# print(next_greatest_letter(letters, 'a'))
# print(next_greatest_letter(letters, 'd'))
# print(next_greatest_letter(letters, 'y'))

# '''
# Problem 5: Find K Closest Planets
# Approach: here, because the array is sorted, we do not need to find k individual planets, but we just need to find the start index of the window of the k closest planets
# so instead of checking individual planets, we are checking the smallest and largest element in the window of k elements
# there are n-k+1 valid start indices, so we loop through those
# '''

# def find_closest_planets(planets, target_distance, k):
#     left, right = 0, len(planets)-k
#     while left<=right:
#         mid=left+(right-left)//2
#         if target_distance-planets[mid]>planets[mid+k]-target_distance:
#             left=mid+1
#         else:
#             right=mid-1
#     return planets[left:left+k]

# planets1 = [100, 200, 300, 400, 500]
# planets2 = [10, 20, 30, 40, 50]

# print(find_closest_planets(planets1, 350, 3))
# print(find_closest_planets(planets2, 25, 2))

# '''
# Problem 6: Sorting Crystals
# Approach: apply merge sort, which is splitting the list in two, sorting each half, linearly iterate to merge them, then recursively do the same thing again
# '''

# def sort_crystals(crystals):
#     if len(crystals)<=1:
#         return crystals
#     mid=len(crystals)//2
#     left = crystals[:mid]
#     right = crystals[mid:]

#     left_sorted = sort_crystals(left)
#     right_sorted=sort_crystals(right)

#     return merge(left_sorted,right_sorted)

# def merge(left, right):
#     result = []
#     i, j = 0,0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# print(sort_crystals([5, 2, 3, 1]))
# print(sort_crystals([5, 1, 1, 2, 0, 0]))

# '''
# Problem 7: Longest Substring With at Least K Repeating Characters
# Approach: any character in the string whose frequency is less than the target frequency, cannot be part of a substring where the frequency of that character is >= target freq
# so we hack off parts of the string at those bad characters
# then we recurse on the remaining substring
# '''

# from collections import Counter

# def longest_substring(s, k):
#     if len(s) < k:
#         return 0
    
#     counts = Counter(s)
#     sub_results = []
#     for char, freq in counts.items():
#         if freq<k:
#             pieces = s.split(char)
#             for piece in pieces:
#                 sub_answer=longest_substring(piece, k)
#                 sub_results.append(sub_answer)
#             return max(sub_results)
#     return len(s)
    

# print(longest_substring("tatooine", 2))
# print(longest_substring("chewbacca", 2))