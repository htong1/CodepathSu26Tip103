'''
Problem 1: Balanced Art Collection
'''

# def find_balanced_subsequence(art_pieces):
#     freq = {}
#     current_sum = 0
#     max_sum = 0
#     for element in art_pieces:
#         if element not in freq:
#             freq[element] = 1
#         else:
#             freq[element]+=1
#     for key, value in freq.items():
#         if key+1 in freq:
#             current_sum = value+freq[key+1]
#             if current_sum>max_sum:
#                 max_sum=current_sum
#     return max_sum

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))


# '''
# Problem 2: Verifying Authenticity
# Approach: base[n], where n is the largest consecutive element in the array
# so the length of the authentic array is always 1+n
# check the frequency of n is 2 and the rest is 1 and check every element in 1 ... n
# '''
# from collections import Counter

# def is_authentic_collection(art_pieces):
#     sorted_art = sorted(art_pieces)
#     n = sorted_art[len(sorted_art)-1]
#     if len(sorted_art) != n+1:
#         return False
#     freq = Counter(art_pieces)
#     for key,value in freq.items():
#         if value != 2 and key == n:
#             return False
#         elif value != 1 and key > n:
#             return False
#         elif value != 1 and key < 1:
#             return False
#     return True

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))

'''
Problem 3: Gallery Wall
Approach: so get the frequency of the items in the 2D array
then build the wall row by row until the frequency of all items is 0
for each row, loop through the map and add each element to the list
as you add to the current list, decrement the frequency in the map
if the frequency is 0, delete the entry from the map
once you reach the end of the map, append the list to the 2D list
keep going until the map is empty
'''

from collections import Counter

#can't delete while iterating through the map; Modifying a dictionary's size while iterating over it directly raises a RuntimeError. Always iterate over a copy (list(freq.keys())) or collect changes to apply after the loop. 
# def organize_exhibition(collection):
#     freq = Counter(collection)
#     result = []
#     while len(freq) > 0:
#         row = []
#         for key,value in freq.items():
#             if value > 0:
#                 row.append(key)
#                 value-=1
#                 if value == 0:
#                     del freq[key]
#         result.append(row)
#     return result

# def organize_exhibition(collection):
#     freq = Counter(collection)
#     result = []
#     while len(freq) > 0:
#         row = []
#         deleted = []
#         for key,value in freq.items():
#             if value > 0:
#                 row.append(key)
#                 value-=1
#                 freq[key] = value
#                 if value == 0:
#                     deleted.append(key)
#         result.append(row)
#         for element in deleted:
#             del freq[element]
#     return result

# collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
#               "Kahlo", "O'Keefe"]
# collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

# print(organize_exhibition(collection1))
# print(organize_exhibition(collection2))

# '''
# Problem 4: Gallery Subdomain Traffic
# Approach: using a map, where the key is the domain and the frequency is the number of times visited
# for each string in domains, split by period
# if there is a new domain, add that domain and the number before it
# if it is not a new domain, add the number before it to the existing domain entry
# to find domain, I can split by period; to get the count, I can split by period?
# '''

# def subdomain_visits(cpdomains):
#     result = []
#     freq = {}
#     for element in cpdomains:
#         count_and_domain = element.split(" ")
#         count = int(count_and_domain[0])
#         domain = count_and_domain[1]
#         domains = domain.split(".")
#         for i in range(len(domains)):
#             subdomain = ".".join(domains[i:])
#             if subdomain not in freq:
#                 freq[subdomain] = count
#             else:
#                 freq[subdomain]+=count
#     for key, value in freq.items():
#         result.append(str(value) + " " + key)
#     return result
    



# cpdomains1 = ["9001 modern.artmuseum.com"]
# cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
#               "1 contemporary.gallery.com", "5 medieval.org"]

# print(subdomain_visits(cpdomains1))
# print(subdomain_visits(cpdomains2))

# '''
# Problem 5: Beautiful Collection
# Approach: get all substrings by using a for loop with increasing index using double pointer method, with one pointer going until the end, and then the next pointer starts
# while doing this, count the frequencies and stuff of each character int he substring and thensum the difference?
# '''

# from collections import Counter

# def beauty_sum(collection):
#     total = 0
#     length = len(collection)
#     for i in range(length):
#         for j in range(i+1,length+1):
#             current = collection[i:j]
#             freq = Counter(current)
#             max_f = max(freq.values())
#             min_f = min(freq.values())
#             total+=(max_f-min_f)
#     return total


# print(beauty_sum("aabcb")) 
# print(beauty_sum("aabcbaa"))

# '''
# Problem 6: Counting Divisible Collections in the Gallery
# Approach: find all subarrays, find the sum within each subarray, and then add to count if the sum of subarray is divisible by k
# '''

# def count_divisible_collections(collection_sizes, k):
#     count = 0
#     length = len(collection_sizes)
#     for i in range(length):
#         for j in range(i+1, length+1):
#             subarr = collection_sizes[i:j]
#             sum = 0
#             for element in subarr:
#                 sum+=element
#             if sum%k == 0:
#                 count+=1
#     return count

# nums1 = [4, 5, 0, -2, -3, 1]
# k1 = 5
# nums2 = [5]
# k2 = 9

# print(count_divisible_collections(nums1, k1))  
# print(count_divisible_collections(nums2, k2))  


# '''
# Problem 1: Cook Off
# Approach: find the freq of all of the ingredients in the target meal and the freq of ingredients in the ingredients string
# for each ingredient, how many meals I can make and then take the min
# '''

# from collections import Counter

# def max_attempts(ingredients, target_meal):
#     freq_in = Counter(ingredients)
#     freq_meal = Counter(target_meal)
#     min_meals = float('inf')
#     for key, value in freq_in.items():
#         if key in freq_meal:
#             current = value//freq_meal[key]
#             if current < min_meals:
#                 min_meals = current
#     return min_meals


# ingredients1 = "aabbbcccc"
# target_meal1 = "abc"

# ingredients2 = "ppppqqqrrr"
# target_meal2 = "pqr"

# ingredients3 = "ingredientsforcooking"
# target_meal3 = "cooking"

# print(max_attempts(ingredients1, target_meal1))
# print(max_attempts(ingredients2, target_meal2))
# print(max_attempts(ingredients3, target_meal3))

# '''
# Problem 2: Dialogue Similarity
# Approach: check if two arrays have the same length; if not, return false
# if yes, use one loop to loop thorugh both. if they have the same words, keep going
# if not, check if both are in similar pairs
# '''

# def is_similar(sentence1, sentence2, similar_pairs):
#     if len(sentence1) != len(sentence2):
#         return False
#     for i in range(len(sentence1)):
#         if sentence1[i] != sentence2[i]:
#             pair = [sentence1[i], sentence2[i]]
#             if pair not in similar_pairs:
#                 return False
#     return True

# sentence1 = ["my", "type", "on", "paper"]
# sentence2 = ["my", "type", "in", "theory"]
# similar_pairs = [ ["on", "in"], ["paper", "theory"]]

# sentence3 = ["no", "tea", "no", "shade"]
# sentence4 = ["no", "offense"]
# similar_pairs2 = [["shade", "offense"]]

# print(is_similar(sentence1, sentence2, similar_pairs))
# print(is_similar(sentence3, sentence4, similar_pairs2))

'''
Problem 3: Cows and Bulls
Approach: loop through secret and guess
'''

from collections import Counter

def get_hint(secret, guess):
    freq_s = Counter(secret)
    freq_g = Counter(guess)
    cows = 0
    bulls = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls+=1
        elif secret[i] != guess[i] and guess[i] in secret and freq_s[secret[i]] == freq_g[secret[i]]:
            cows+=1
    return str(bulls)+"A"+str(cows)+"B"

secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))

'''
Problem 4: Count Winning Pairings
Approach: get all the pairs using a nested for loop, then sm them and see if they are a power of 2
'''

def count_winning_pairings(star_power):
    count = 0
    for i in range(len(star_power)):
        for j in range(i+1, )
    return

star_power1 = [1, 3, 5, 7, 9]
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))
