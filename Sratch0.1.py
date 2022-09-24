for i in range(5):
    if len(input("Password: ")) <= 8:
        print("Weak Password!")
    else:
        print("Strong Password!")
        break
