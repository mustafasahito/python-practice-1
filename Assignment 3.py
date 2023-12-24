#Half Pyramid
i=1
while i <=5:
    print(i*"*")
    i+=1

#Inverted Half Pyramid
i=5
while i>=1:
    print(i*"*")
    i-=1

#Full Pyramid
i=1
j=5
while i<=5:
    print(j*" "+"* "*i)
    j-=1
    i+=1

#Inverted Full Pyramid
i=5
j=5
while i>=1:
    print(j*" "+" *"*i)
    j+=1  
    i-=1

#Hollow Inverted Half Pyramid
i=5
while i>=1:
    print(i*"* ")
    i-=3
    print(i*"*     ")
    print(i*"*   ")
    print(i*"* ")
    i-=1


#Hollow Full Pyramid
i=0
while i<5:
    j=0
    while j<(5-i-1):
        print(end=" ")
        j+=1
    j=0
    while j<=i:
        if j==0 or j==i or i==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1


#Seccond Pic Exercises
i=1
j=5
while i<=5:
    print(j*" "+"* "*i)
    j-=1
    i+=1
i=4
while i>=1:
    print(j*" "+" *"*i)
    j+=1  
    i-=1


i=10
while i in range(11):
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    print(i*"*  ")
    i+=10

i=4
j=5
while i>=1:
    print(j*" "+" *"*i)
    j+=1  
    i-=1
i=1
while i<=4:
    print(j*" "+"* "*i)
j-=1
i+=1
