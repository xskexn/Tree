#Importing the random folder 
import random
print("Generating otp password")
#Defineing empty list to append the generated number
otpw = []
#Process Function
def password():
    for i in range(5):
        #For loop to add to otpw list 5 number
        pw = random.randint(1111, 9999)
        #generating 4 digits number
        otpw.append(pw)
        ###Appending itrms to the list 
        #print(otpw) //Try it out 
    finalOtp = random.choice(otpw)
    print(str(finalOtp) + " This is your password")
    #Using random choise function and 
    #converting the choise into a string 
    #to print it out
password()