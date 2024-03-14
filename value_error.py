def type_error():

    """convert string to int"""

    user_input = ""
    integer = ""
    while type(integer) != int:
        try:
            user_input = input("Please enter an integer: ")
            integer = int(user_input)
            print(type(integer))
            print(integer)
            
        except(ValueError):
            print("value entered is not an integer.")


def type_error2():

    """Find index in string"""

    input_string = input("Please enter a string: ")
    input_index = int(input("Please input an index integer: "))
    
    try:
        print(input_string[input_index -1])
    except(ValueError):
        print("please enter an Integer")
    except(IndexError):
        print("index out of range")    






type_error()
type_error2()



