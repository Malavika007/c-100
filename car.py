class Car(object):
    def __init__(self, company, model, color, speedlimit):
        self.company = company
        self.model = model
        self.color = color
        self.speedlimit = speedlimit

car1 = Car("Audi", "model 8", "black", "70Km/hr")
car2 = Car("Mercedez", "model Z", "silver", "60Km/hr")
car3 = Car("BMW", "model s", "blue", "100Km/hr")


def start(self):
    print('please select your car!')
    print('car1 ("Audi", "model 8", "black", "70Km/hr")')
    print('car2("Mercedez", "model Z", "silver", "60Km/hr")')
    print('car3("BMW", "model s", "blue", "100Km/hr")')
    car = input('which car? [car1/car2/car3]')

    print('your '+{car.name}+'has started')
    a = input(str('what next? [a for accelerate, s for stop]'))
    if (a == 'a'):
        print("your car is accelerating to"+{car.speedlimit})
    elif (a == 's'):
        print("your car has stoped")
    else:
        print('command not recognised !!')

def game():
    print("Welcome to our car game !!")
    q = input(str('are you ready to start?[y/n]: '))
    if (q=='y'):
        start(self)
    elif (q == 'n'):
        print('ok bye')

game()
       





