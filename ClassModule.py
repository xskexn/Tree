class phone:
    def __init__(self, name, price, brand, ram, rom,):
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.rom = rom
        def cost(self, price):
            if self.price >= 500:
                return True
            else:
                return False
class shoes:
    def __init__(self, name, price, type, color):
        self.name = name
        self.price = price
        self.type = type
        self.color = color
class user(phone):
    def __init__(self, username, email, password, name, lastname, gpa):
        self.lastname = lastname
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.gpa = gpa
class chef():
    def makepasta(self):
        print("chef makes pasta")
    def makespaghetti(self):
        print("chef makes spaghetti")
class chinesechef(chef):
    def makesalsa(self):
        print("chef makes salsa")
    def makesalad(self):
        print("chef makes salad")
class friend():
    def __init__(self, name, surname, age, partner):
        self.name = name
        self.surname = surname
        self.age = age
        self.partner = partner