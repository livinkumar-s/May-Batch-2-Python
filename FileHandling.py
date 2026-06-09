with open("text1.txt",'a') as f:
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    print(name,age)
    f.write(f"Name: {name}\nAge: {age}\n")

print("The process is over...!")


# file=open("text.txt",'r')
# content=file.readline()
# content=file.readline()
# content=file.readline()
# content=file.readline()
# content=file.readlines() #list
# content=file.readline()
# file.seek(10)
# content=file.read(10)

# print(content)
# print(file.tell())
# file.close()

# file = open("text.txt",'w')

# print(file.writable())

# content='''Mahendra Singh Dhoni born 7 July 1981 is an Indian
#  professional cricketer who plays as a right-handed 
#  batter and a wicket-keeper. Widely regarded as one of 
#  the most prolific wicket-keeper batsmen and captains, he represented the Indian cricket team and was the captain of the team in limited overs formats from 2007 to 2017 and in Test cricket from 2008 to 2014.
#    Dhoni has captained the most international matches and is the most successful Indian captain. He has led India to victory in the 2007 ICC World Twenty20, the 2011 Cricket World Cup, and the 2013 
#    ICC Champions Trophy, being the only captain to win three different limited overs ICC tournaments. He also led the teams that won the Asia Cup in 2010 
#    and 2016, and he was a member of the title winning squad in 2018'''


# file.write(content)

# file.close()

# file = open("text.txt",'a')

# # print(file.writable())

# content='''
# Mahendra Singh Dhoni born 7 July 1981 is an Indian
#  professional cricketer who plays as a right-handed 
#  batter and a wicket-keeper. Widely regarded as one of 
#  the most prolific wicket-keeper batsmen and captains, he represented the Indian cricket team and was the captain of the team in limited overs formats from 2007 to 2017 and in Test cricket from 2008 to 2014.
#    Dhoni has captained the most international matches and is the most successful Indian captain. He has led India to victory in the 2007 ICC World Twenty20, the 2011 Cricket World Cup, and the 2013 
#    ICC Champions Trophy, being the only captain to win three different limited overs ICC tournaments. He also led the teams that won the Asia Cup in 2010 
#    and 2016, and he was a member of the title winning squad in 2018'''


# file.write(content)

# file.close()


# file=open("text1.txt","x")
# file.close()

