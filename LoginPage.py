import os
command = None
outpw = False
outuser = False
info = ["Your info"]
###start###
print("Hi and Welcome to Unix" + "\n" "Please register")
print("Please input your infos ")
name = input("Name: ")
username = input("Username: ")
email = input("Email: ")
password = input("Hi "+username+" Input a Password" + "\n" "Password: ")
info.extend(name)
info.append(username)
info.append(email)
info.append(password)
print("Remeber your email and password" + "\n" "Now please log in")
while not outuser and not outpw:
    logusername = input("Username: ")
    if logusername == username:
        outuser = True
        print("Username correct!")
    elif logusername != username:
        print("Incorect username")
    logpw = input("Password: ")
    if logpw == password:
        outpw = True
        print("Password correct!")
    elif logpw != password:
        print("Incorrect password")
while outpw and outuser:
    while command != "log out":
        command = input("Command Please:> ")
        if command == "calculator":
            from file import Calculator
            calculator = Calculator()
            calculator.logincalculator()
        elif command == "os":
            os.system("notepad.exe") 
        elif command == "age":
            try:
                age = int(input("Input Your Age: "))
            except:
                print("Input a valid age")
                year = 2020
            if age >= year:
                print("Invalid age")
            else:
                print(year - age)
        elif command == "date":
            import datetime
            time = datetime.date.today()
            print("today is the " + str(time))
        elif command == "log out":
            print("Goodbye " + name)
        elif command == "info":
            print(info)
        else:
            print("Hey please input a valid key")