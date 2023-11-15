# Unspecified number of parameters
def add(*args):
    print(args[1])
    sun = 0
    #print(args) Just print a tuple in this case
    for n in args:
        sun += n
    return sun


print(add(2,3,4,5,6,7,8))

def calculate(n,**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key, value)
        print(kwargs["add"])
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)

calculate(2,add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # Caso não seja atribuído um valor na chamada, o get atribui None
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Volkswagen")
print(my_car.make)