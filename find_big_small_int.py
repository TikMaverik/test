import random
list1 = []

def find_max(nums):
    """Find largest int in list"""
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

def find_min(nums):
    """Find smallest int in list"""
    min_num = float("inf") # larger than all other numbers
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


for i in range(0, 100000000):
    number = random.randint(1, 1000000000)
    list1.append(number)

print("Largest int in list: ", find_max(list1))
print("Smallest int in list: ", find_min(list1))
# print(list1)


    