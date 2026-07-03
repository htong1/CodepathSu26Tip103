'''
Problem: Recursive Digit Sum
Approach: first, initially multiply the given string by k and then sum the digits before doing anything recursively
then, recursively pass in the sum until the total is less than 10
'''

def superDigit(n, k):
    # Write your code here
    first_digit_sum = 0
    for char in n:
        first_digit_sum+=int(char)
    
    first_digit_sum = first_digit_sum*k

    return helper(first_digit_sum)

def helper(n):
    if n < 10:
        return n
    
    digit_sum=0
    for char in str(n):
        digit_sum += int(char)
    return helper(digit_sum)

