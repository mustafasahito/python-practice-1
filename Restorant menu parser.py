#7. Restaurant Menu Parser:
#Write a program that reads a restaurant menu file (text or CSV) and stores 
#items, prices, and categories in a dictionary.
#Allow users to browse by category or search for specific items.f
food={
    "sweet":{"custer":200,"kheer":250,"vermicili":150},
    "spicy":{"chillifry":120,"salty food":150},
    "drinking":{"Juice":100,"bottle":100}
}
choice=input("enter which category food you want \t 1.sweet \t 2.spicy \n 3.drinking:")
print(food[choice])
choice=input("enter what you want to order")
print(choice,"is being ready for you")
