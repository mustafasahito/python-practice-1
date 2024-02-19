#5. Temperature Converter:
#Build a program that converts temperatures between Celsius and 
#Fahrenheit using a dictionary to store conversion factors.
temperature_container={}
def temperature_converter():
    celsius=int(input("enter the temperature in celsius to convert in farhneit:"))
    farhneit=(celsius*9/5)+32  #formula to convert celsius in farhneit
    temperature_container[celsius]=farhneit
    choice=input("do you check some more temperature values(yes/no):")
    if choice.lower()=="yes":
        temperature_converter()
    elif choice.lower()=="no":
        print("Thanks")
    else:
        print("INVALID CHOICE")
temperature_converter()
print("you will see values like this celsius:farhneit",temperature_container)
