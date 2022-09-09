import random
otpList = []
for i in range(4):
    otpChoice = random.randint(1111,9999)
    otpList.append(otpChoice)
print(otpList)
otpw = random.choice(otpList)
print(otpw)
