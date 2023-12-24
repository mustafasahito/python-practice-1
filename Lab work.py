#Exercise:1
num=int(input("Enter a number:"))
if num%2==0:
    print("Number is Even")
else:
    print("Number is odd")

#Exercise:2
age=int(input("Enter your age:"))
if age>=18:
    print("You are Adult")
else:
    print("You arenot Adult")

#Exercise:3
username="Musawer"
password="1917"

enter_username=input("Enter yor username:")
enter_password=input("Enter your password:")

if enter_username==username and enter_password==password:
    print("logged in successfully")
else:
    print("Login failed")

#Exercise:4
num=int(input("Enter a number:"))
if num>0:
    print("Given number is Positive.")
elif num<0:
    print("Given NUmber is Negative.")
if num==0:
    print("Given Number is Zero.")

#Exercise:5
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
num3=int(input("Enter a number3:"))

if num1<num2 and num2<num3:
    print(num3,"is Greater")
elif num1<num2 and num2>num3:
    print(num2,"is Greater")
else:
    print(num1,"is Greater")


#Exercise: 6
max_number=0

for i in range(10):
    number=int(input(f"Enter number for{i}:"))
    if number>max_number:
        max_number=number
    print(f"{max_number}is greater")

print(f"Maximuim NUmber is:{max_number}")

#Exercise:7
max_number=0

for i in range(20):
    number=int(input(f"Enter number for{i}:"))
    if number>max_number:
        max_number=number
    print(f"{max_number}is greater")

print(f"Maximuim NUmber is:{max_number}")

#Exercise: 8
num=int(input("Enter a number:"))
sum=0
i=1
while i<= num:
    sum+=i
    i+=1
print("The sum of natural numbers up to", num,"is",sum)

#Exercise: 9
name=input("Enter your name:")
v=['a','e','i','o','u']
count=0
for i in name:
    if i in v:
        count+=1

print(f"{count}")
