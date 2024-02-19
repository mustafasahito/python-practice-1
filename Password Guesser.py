#3. Shopping List Manager:
#Develop a program that allows users to add, remove,and 
#check off items on a shopping list stored in a dictionary
shoppinglist={
    "sweets":"0.5kg",
    "apples":"1kg",
    "tomatoes":"1kg",
    "potatoes":"3kg",
    "spicy":"0.75kg",
    "rices":"6kg",
    "meat":"2kg",}
choice=input("enter do you want to see the shopping list(yes/no)")
if choice.lower()=="yes":
    print(shoppinglist)
    newitem=input("which atom quantity you want to change(or add) in your list")
    newquantity=input("how much you want to keep its quantity")
    shoppinglist[newitem]=newquantity
    modify=input("tell which element you want to remove")
    try:
        del shoppinglist[modify]
    except:
        print(f"{modify} is not in list see its spelling again")
    print("mdified shopping list is ",shoppinglist)
elif choice.lower()=="no":
    print("thanks")
else:
    print("INVALID CHOICE")