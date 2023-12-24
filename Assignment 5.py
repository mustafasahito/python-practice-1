#Exercise: 1

for i in range(11):
    print(i)

#Exercise:2

num=int(input("Enter a number:"))
print("Multiplication table for",num,":")
for i in range(1,11):
    result=num*i
    print(num,"x",i,"=",result)

#Exercise: 3

num=int(input("Enter a number:"))
sum=0
i=1
while i<= num:
    sum+=i
    i+=1
print("The sum of natural numbers up to", num,"is",sum)

#Exercise: 4

names=("Musawer","Musaib","Sarfaraz","Aaliyan","Gul Muneer")
for name in names:
    print(names)

#Exercise: 5

num=int(input("Enter a number:"))
factorial=1
i=1
while i<=num:
    factorial*=i
    i+=1
print("The factorial of",num,"is",factorial)

#Exercise:6

num_terms=int(input("Enter number of terms:"))
first_term=0
second_term=1
print(first_term,end="")
print(second_term,end="")
for i in range(2,num_terms):
    next_term=first_term+second_term
    print(next_term,end="")
    first_term=second_term
    second_term=next_term

#Exercise: 7

num=int(input("Enter a Number:"))
reversed_num=0
while num>0:
    last_digit=num%10
    reversed_num=(reversed_num*10)+last_digit
    num=num//10
print("Reversed Number:", reversed_num)

#Exercise: 8

string=input("Enter a string:")
vowel_count=0

for char in string:
    if char.lower()in"aeiou":
        vowel_count+=1
print("Number of Vowels:",vowel_count)

#Exercise: 9

number=int(input("Enter a NUmber:"))
copy_number=number
reversed_number=0

while copy_number>0:
    last_digit=copy_number%10
    reversed_number=(reversed_number*10)+last_digit
    copy_number=copy_number//10

if number==reversed_number:
    print("The number is a palindrome!")
else:
    print("The number isnot a palindrome.")

#Exercise: 10

sum_of_squares=0
for num in range(1,6):
    square=num**2
    sum_of_squares+=square
print("The sum of the squares from 1 to 5 is:",sum_of_squares)
