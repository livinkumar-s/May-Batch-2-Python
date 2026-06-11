class Bottle:
    #attributes
    color="Blue"
    def __init__(self,name,rad,height):
        self.name=name
        self.radius=rad
        self.height=height 
    def showVolume(self): #b2
        print((22/7)*self.radius*self.radius*self.height)
    def open(self, opener):
        print(f"Bottle {self.name} is opening...! By {opener}" )
    @classmethod
    def showColor(cls):
        print(cls.color)
    @staticmethod
    def sayHello():
        print("Hello...!")

# Bottle.sayHello()


# Bottle.showColor()

b1=Bottle("Aqua",32,200)
# b1.open("Leo")

a=10
b="Hello"
c=[1,2,3,4,5]

# print(type(a))


# b1.showVolume() #Bottle.showVolume(b1)

# b2=Bottle("Benjamin",28,300)

# b2.showVolume() #Bottle.showVolume(b2)

# Bottle.color="Black"
# Bottle.showVolume(b1)

# 3 attributes, 1 method

# b1=Bottle()
# print(b1.name)

# b2=Bottle()
# print(b2.name)


# print(b2.name)

# b1.showVolume()
# b2.showVolume()

# print(b1.color)
# print(b2.color)