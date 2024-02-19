#6. Phonebook Organizer:
#Create a program that stores names and phone numbers in a dictionary.
#Offer options to add, search, and update contacts.
contactbook={}
def Phonebook_Organizer():
    choice=int(input("enter what you want to do \n 1.add new contact \t 2.update contact list \n 3.search a contact \n 4.view contact list \n (enter 1,2,3 or 4):"))
    if choice==1:
        new=input("enter the name of contact:")
        newphone=int(input(f"enter phone number of {new}:"))
        contactbook[new]=newphone
    elif choice==2:
        update=input("enter the contact name that is to be updated")
        updatednumber=int(input(f"enter new number of {update}"))
        contactbook[update]=updatednumber
    elif choice==3:
        search=input("enter contact whom you want to view")
        try:
            print(contactbook[search])
        except:
            print(f"{search} is not in contactbook")
    elif choice==4:
        print(contactbook)
    else:
        print("INVALID CHOICE")
    confirm=input("do you want to do this again(yes/no)")
    if confirm.lower()=="yes":
        Phonebook_Organizer()
    else:
        print("OK")
Phonebook_Organizer()        