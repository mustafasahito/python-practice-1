
#Exercie1
cost=0
for i in range(3):
    quantity=int(input("Enter quantity:"))
    price=int(input("Enter price:"))
    total=quantity*price
    cost+=total
print("Total cost is:",cost)
if cost>100 and cost<200:
    discount=cost*0.05
    total=cost-discount
    print("total amount is:",total)
elif cost>200:
    discount=cost*0.1
    total=cost-discount
    print("Total amount is:",total)

#Exercise2
celcius=int(input("Enter tempreture in celcius:"))
if celcius<0:
    print("Wear Warm Clothes")
elif celcius>30:
    print("Stay Hydrated")

#Exercise3
lst=[ ]
for i in range(3):
    name=input("Enter a Name:")
    lst.append(name)
print(lst)
check_name=input("Enter name to check:")
if check_name in lst:
    print(check_name,"is in List")
else:
    print(check_name,"is not in List")

#Exercise4
def factorial(num1):
    if num1==0 or num1==1:
        return 1
    else:
        return num1*factorial(num1-1)
result=factorial(5)
print("The Factorial of 5 is:",result)

#Exercise5
def is_palindrome(word):
    word=word.lower()
    if word==word[::-1]:
        print(word,"Is palindrome")
    else:
        print(word,"Is not palindrome")
print(is_palindrome("Level"))
print(is_palindrome("Python"))

#Exercise6
inventory=[ ]
def add_item():
    name=input("Enter item Name:")
    quantity=int(input("Enter quantity:"))
    price=float(input("Enter the price:"))

    item={"name":name, "quantity":quantity, "price":price}
    inventory.append(item)
    print("Item Addded Successfully")
def print_inventory():
    print("Inventory:")
    total_value=0

    for item in inventory:
        name=item['name']
        quantity=item['quantity']
        price=item['price']

        value=quantity*price

        print(f"{name}-Quanttity:{quantity},Price:${price},Value:${value}")

        total_value+=value
    print("Total value of inventory:$",total_value)

while True:
    print("1.Add item")
    print("2. Print inventory")
    print("3. Exit")

    choice=input("Enter your Choice(1-3):")
    if choice=="1":
        add_item()
    elif choice=="2":
        print_inventory()
    elif choice=="3":
        print("Exiting program..")
        break
    else:
        print("Envalid choice. Please Try again")

#Exercise7
def filter_even_squares(numbers):
    even_squares=[ ]
    for num in numbers:
        square=num**2
        if square%2==0:
            even_squares.append(square)
    return even_squares
numbers=range(1,11)
square=[num**2 for num in numbers]
even_squares=filter_even_squares(square)
print(even_squares)

#Real Life Exercises:
#1. Movie Ticket Price:
def calculate_ticket_price(age,day_of_week,num_ticket):
    if age=="adult":
        if day_of_week=="weekday":
            price=500
        elif day_of_week=="weekend":
            price=700
    elif age=="child":
        if day_of_week=="weekday":
            price=300
        elif day_of_week=="weekend":
            price=500
    elif age=="senior":
        if day_of_week=="weekday":
            price=600
        elif day_of_week=="weekend":
            price=800
        
    if num_ticket>=5:
        price*=0.9
    elif num_ticket>=10:
        price*=0.8
    return "${:.2f}".format(price)

#Usage:
ticket_price=calculate_ticket_price("adult","weekday",7)
print("Total ticket price is:",ticket_price)

# 2.Restaurent Bill calculator
def calculate_total_bill(items,quantities,prices,discount_percentage=0,tax_percentage=0,num_friends=1):
    subtotal=0
    for i in range(len(items)):
        subtotal+=quantities[i]*prices[i]
    
    discount=subtotal*(discount_percentage/100)
    subtotal-=discount

    tax=subtotal*(tax_percentage/100)
    total=subtotal+tax
    
    if num_friends>1:
        total_per_friend=total/num_friends
        return total_per_friend
    else:
        return total
#usage:
items=["Pizza","Parathas","Chae"]
quantities=[3,6,6]
prices=[500,240,180]
discount_percentage=10
tax_percentage=7.5
num_friends=3
total_bill=calculate_total_bill(items,quantities,prices,discount_percentage,tax_percentage,num_friends)
print("Total bill amount per friend is:",total_bill)

# 3. Social Media Post Analyzer:


# 4. Travel Cost Estimator:
def estimate_travel_cost(destination,transportation,accommodation,activities):
    transport_cost=0
    accommodation_cost=0
    activities_cost=0

    if transportation=="flight":
        transportation_cost=500
    elif transportation=="train":
        transport_cost=300
    elif transportation=="bus":
        transport_cost=100

    if accommodation=="hotel":
        accommodation_cost=300
    elif accommodation=="hostel":
        accommodation_cost=200
    elif accommodation=="airbnb":
        accommodation_cost=100

    for activity in activities:
        if activity=="museum":
            activities_cost+=50
        elif activity=="sightseeing":
            activities_cost+=30
        elif activity=="shopping":
            activities_cost+=80
    
    total_cost=transportation_cost+accommodation_cost+activities_cost
    return total_cost
#Usage:
destination="karachi"
transportation="bus"
accommodation="hotel"
activities=["museum","shopping"]

estimated_cost=estimate_travel_cost(destination,transportation,accommodation,activities)
print("Estimated travel cost:",estimated_cost)
