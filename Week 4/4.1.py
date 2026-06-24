

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

def calculate_fabric_waste(items, fabric_rolls):
    print(fabric_rolls)
    total = 0
    for item, num in items:
        total += num
    
    return sum(fabric_rolls) - total
    

items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls = [5, 5, 5]
print(calculate_fabric_waste(items, fabric_rolls))

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls = [4, 4, 4]
print(calculate_fabric_waste(items_2, fabric_rolls))

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls = [7, 5, 5]
print(calculate_fabric_waste(items_3, fabric_rolls))