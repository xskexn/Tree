#Simple calculator LCW.inc Ken. E. Igb.
class Calculator():
    def logincalculator(self):
        print("Hi Welcome to the calculator")
        #Define your integers
        try:
        #Try block to overcome program damage
            num1 = int(input("Input first number: "))
        except ValueError:
            print("Input valid number")
        #Input function to define operator 
        op = input("Input operator: ")
        try:
        #Try block to overcome program damage
            num2 = int(input("Input second number: "))
        except ValueError:
            print("Input valid number")
        #Result calculator process
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "*":
            print(num1 * num2)
        else:
        #Overcome Error
            print("invalid operator please input key like >(+,-,*,/)")