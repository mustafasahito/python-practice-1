#Question.1
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
result=(num1*num1)+(num2*num2)
if num1%2==0 and num2%2==0:
    print(result)
else:
    print("Can't Calculates The Values")

#Question.2
num=int(input("Enter a Number To Find Factorial:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
    elif num<0:
        print("Given Number is Invalid")

#Question.3
for i  in range(5):
    Number=int(input("Guess a Nnumber:"))
    import random
    num=random.randint(1,100) 
    print(num)
    if Number==num:
        print("Correct Answer! You win The Game")
    elif Number>num:
        print("Too High")
    elif Number<num:
        print("Too Low")

#Question.4
Number_of_people=int(input("Enter Number of Peoples:"))
Total_Meals=int(input("Enter Number Of Meals:"))
Cost_of_each_meal=int(input("Enter price of one meal:"))
Sales_tax_percentage=int(input("Enter sales tax:"))
Tip_percentage=int(input("Enter Tip:"))
Sales_Tax=Sales_tax_percentage*Cost_of_each_meal*Total_Meals//100
Tip_Amount=Tip_percentage*Cost_of_each_meal*Total_Meals//100



print(f"Total Cost Of Food Is:",Cost_of_each_meal*Total_Meals)
print(f"Total Sales Tax:",Sales_Tax)
print(f"Total tip Amount:",Tip_Amount)
print(f"Total Bill Amount per Person:",Cost_of_each_meal*Total_Meals//Number_of_people)

