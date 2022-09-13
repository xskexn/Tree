weak = True
count = 0
while weak and count <= 5:
    password = input("Password: ")
    lenght = len(password)
    if lenght <= 8:
        weak = True
        count +=1
        print("Weak Password!")
    else:
        weak = False
        print("Strong Password!")