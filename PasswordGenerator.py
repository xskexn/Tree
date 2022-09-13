import random
pwlen = int(input("How many characters should the password have? "))
#pwlen /= 2
password = []
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
specialChar = [",",".","/","*","@","[","]","{","}","`","-","_","=","+","|","?","!"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
for n in range(pwlen):
    password.append(random.choice(lowerLetters))
    password.append(random.choice(upperLetters))
    password.append(random.choice(specialChar))
    password.append(random.choice(numbers))
    #print(password)
    random.shuffle(password)
finalpassword = "".join(password)
finalpassword = finalpassword[0:pwlen]
print(finalpassword)