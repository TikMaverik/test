my_tuple = ((1, 2), (3, 4))
j = 0
for i in my_tuple:
    j += 1
    sum = i[0] + i[1]
    print(f"Row {j} sum: {sum}")

numbers = [4,3,2,1]
numbers2 = numbers[:]
numbers.sort()
print(numbers)
print(numbers2)