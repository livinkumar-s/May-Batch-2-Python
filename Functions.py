# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")

# printSteps()
# printSteps()
# printSteps()

# print()
# input()
# list()

# def findSum(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#     print(a+b+c)

# findSum(b=5,c=4,a=3)

# def findPro(x,y,z=10):
#     print(x*y*z)

# findPro(2,3,4)

# def findPro(*a):
#     ans=1
#     for i in a:
#         ans*=i 
#     print(ans)

# findPro(4,3)

# def collectData(**a):
#     print(a)

# collectData(name="ben",age=44)

# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     return
#     print("Step4")
#     print("Step5")

# a=printSteps() #caller
# print(a)

# print("Hello")
# a=input("Enter your number: ")
# print(a)

# def printMul(num1,num2):
#     print(num1*num2)

# print(printMul(2,2))

# def fact(num):
#     if num==1:
#         return  1
#     return num*fact(num-1)

# num=5
# # return 5 * 4 * 3 * 2 * 1

# print(fact(5))

# a=15

# def dummy():
#     a=10
#     print(a)

# dummy()
# print(a) # 15

age=22

def incAge():
    global age
    age+=1

incAge()
incAge()
incAge()
incAge()
incAge()
incAge()
incAge()
print(age)