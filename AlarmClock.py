import random
pwlen = int(input("How many characters should the password have? "))
#pwlen /= 2
password = []
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
specialChar = [",",".","/","*","@","[","]","{","}","`","-","_","=","+","|","?","!"]
for n in range(int(pwlen)):
    password.append(random.choice(lowerLetters))
    password.append(random.choice(upperLetters))
    password.append(random.choice(specialChar))
    numbers = random.randint(0,9)
    password.append(numbers)
#print(password)
    random.shuffle(password)
    password = str(password)
    finalpassword = "".join(password)
print(finalpassword)