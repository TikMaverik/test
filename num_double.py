def doubles(num):
    """doubles number entered by the user"""
    doubled_num = num + num
    return doubled_num

num_double = float(input("Enter  number to double: "))

for i in range(1, 4):
    num_double = doubles(num_double)
    print(num_double)
    