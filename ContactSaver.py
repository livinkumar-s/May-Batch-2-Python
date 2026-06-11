import mysql.connector

c1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="contactsaver"
)

print("Connected successfully")
cursor=c1.cursor()
# cursor.execute("SELECT * FROM contacts")
# result=cursor.fetchall()
# cursor.execute("UPDATE contacts SET mobile=%s WHERE id=%s",["6367687666",1])
# c1.commit()
# print("Done")

def addContact(name,mobile):
    if(not mobile.isdigit() or len(mobile)!=10):
        print("Please provide valid Number")
        return
    try:
        cursor.execute("INSERT INTO contacts (name,mobile) VALUES (%s,%s)",[name,mobile])
        c1.commit()
        print("Added Successfully")
    except Exception:
        print("Something went Wrong")

def viewContact():
    try:
        cursor.execute("SELECT * from contacts")
        for x,y,z in cursor.fetchall():
            print(f"{y}: {z}")
        print("-------------------------")
    except Exception:
        print("Something went wrong...!")
def updateContact():
    searchTerm=input("Search the contact: ")
    try:
        cursor.execute("SELECT * FROM contacts WHERE name LIKE %s or mobile like %s",[f"%{searchTerm}%",f"%{searchTerm}%"])
        fetchedRecords=cursor.fetchall()
        for x,y,z in fetchedRecords:
            print(f"{y}: {z}. id: {x}")
        if len(fetchedRecords)<1:
            print("No Matching Records")
            return
        id=int(input("Choose the id of contact you wanna update: "))
        person=None
        for i,j,k in fetchedRecords:
            if i==id:
                person=(j,k)

        name=input(f"Enter Name({person[0]}): ")
        mobile=input(f"Enter Mobile({person[1]}): ")

        if name=="":
            name=person[0]
        if mobile=="":
            mobile=person[1]

        cursor.execute("UPDATE contacts SET name=%s, mobile=%s WHERE id=%s",[name,mobile,id])
        c1.commit()
        print("Updation Successfull...!")
        print("----------------------------")

    except Exception:
        print("Something went wrong...!")
def deleteContact():
    pass

while 1:
    inp=int(input('''0-->Exit
1-->Add Contact
2-->View All Contact
3-->Update Contact
4-->Delete Contact
Choose an Option: '''))
    
    if inp==0:
        break
    elif inp==1:
        name=input("Enter Name: ")
        mobile=input("Enter Mobile: ")
        addContact(name,mobile)
    elif inp==2:
        viewContact()
    elif inp==3:
        updateContact()
    elif inp==4:
        deleteContact()
