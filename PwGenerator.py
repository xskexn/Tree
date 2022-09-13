import random
#imported the random library to randomly choose diffrent Character from list below
print("Password Generator!")
#list that contain all the Character
char =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"1","2","3","4","5","6","7","8","9","0",
"!","(","?",")","%","/","&","$","@"]
#Lists used to append all the random selected Character
passwordList=[]
#Defult passowrd lenght in case user don't input the lenght
count = 8
#user input to ask how long yhe passoword should be
try:
    count = int(input("How long do you want the password? :> "))
except ValueError:
    print("You shold try to input a number if you want a choose your lenght!" + "\n" + "Anyway...")
#function for pw creation
def passwordMod(count):
    #the var "count" is the pw lenght the parameter of the function is 8 by default 
    #the user overwrite the "count" by before executing the function
    for i in range(count):
        passwordSel = random.choice(char)
        passwordList.append(passwordSel)
        #the selectedm char are all appended to a list then joined togheter creating a password
        password = "".join(passwordList)
    print("Here is your password: " + password)
passwordMod(count)