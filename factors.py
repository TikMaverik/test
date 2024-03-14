def factors(number):
    """Give factors for number entered"""
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            print(f"{divisor} is a factor of {number}")


factors(int(input("Please enter a number to test for Factorials: ")))