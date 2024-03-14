def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return F

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return C

temp_far = float(input("enter temperature in Fahrenheit: "))

temp_cel = convert_far_to_cel(temp_far)

print(f"{temp_far} degrees F = {temp_cel:.2f} degrees C")

temp_cel = float(input("enter temperature in Celcius: "))

temp_far = convert_cel_to_far(temp_cel)

print(f"{temp_cel} degrees C = {temp_far:.2f} degrees F")