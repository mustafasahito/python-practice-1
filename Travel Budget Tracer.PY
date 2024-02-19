#10. Travel Budget Tracker:
#Create a program that allows users to track their travel 
#expenses by category (e.g., transportation, accommodation, food).
#Use a dictionary to store categories and their corresponding expenses.
dictionary={
    "transport":{"7days expense":""},
    "accomodation":{"7days expense":""},
    "food":{"7days expense":""}
}
sum_transport=0
sum_accomodation=0
sum_food=0
for i in range(7):
    transport=int(input(f"enter your expenses of day{i+1} on transport"))
    accomodation=int(input(f"enter your expenses of day{i+1} on accomodation"))
    food=int(input(f"enter your expenses of day{i+1} on food"))
    sum_transport+=transport
    sum_accomodation+=accomodation
    sum_food+=food
    
    
dictionary["transport"]["7days expense"]=sum_transport
dictionary["accomodation"]["7days expense"]=sum_accomodation
dictionary["food"]["7days expense"]=sum_food
choice=input("enter which category of expenses you want to view(transportation,accomodation,food)")
print(dictionary[choice])


