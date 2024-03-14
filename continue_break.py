

def breaktest():
    user_input = ""   
    while (user_input != "q") and (user_input != "Q"):
        user_input = input("Type \"q\" or \"Q\" to quit: ")
        if user_input.upper() == "Q":
            break
        else:
            print("wrong input")

def continuetest():
    for i in range(51):
        if i % 3 == 0:
            continue
        print(i)


        
breaktest()
continuetest()

#while (user_input != "q") and (user_input != "Q"):