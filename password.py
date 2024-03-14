for n in range(3):
    password = input("Password: ")
    if password == "1234":
        break
    print("Password is incorrect.")
else:
    print("Suspicious activity. The authorities have been alerted.")