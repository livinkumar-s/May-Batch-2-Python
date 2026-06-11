# class Calc:
#     version="1.0.0"
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#     @staticmethod
#     def sub(a,b):
#         print(a-b)

# class SuperCalc:
#     version='1.0.1'
#     @staticmethod
#     def mul(a,b):
#         print(a*b)
#     @staticmethod
#     def div(a,b):
#         print(a/b)

# class ScienceCalc(SuperCalc, Calc):
#     @staticmethod
#     def mod(a,b):
#         print(a%b)
#     @staticmethod
#     def add(a,b,c):
#         print(a+b+c)

# c1=Calc()

# Calc.add(9,9)
# Calc.sub(9,9)

# c1=ScienceCalc()
# c1.add(1,2)

# from abc import ABC,abstractmethod

# class AV(ABC):
#     @abstractmethod
#     def clean():
#         pass

# class Animal(ABC):
#     @abstractmethod
#     def sound():
#         pass

# class Lion(Animal):
#     @staticmethod
#     def showWeight():
#         print("1000lbs")
#     @staticmethod
#     def sound():
#         print("Roar")

# a1=Lion()
# a1.sound() 




# class LeoAntiVirus(AV):
#     @staticmethod
#     def clean(name):
#         print(f"Your PC ({name}) is getting cleaned...")
#         print("No Virus Found..")
#         print("Done")

# class LivAntiVirus(AV):
#     @staticmethod
#     def clean(name):
#         print(f"Your PC ({name}) is getting cleaned...")
#         print("No Virus Found..")
#         print("Done")


# class pc:
#     def __init__(self,name):
#         self.name=name
#     def doClean(self,antiVirusObj):
#         antiVirusObj.clean(self.name)

# av1=LeoAntiVirus()
# av2=LivAntiVirus()
# pc1=pc("Lenovo")

# pc1.doClean(av1)


