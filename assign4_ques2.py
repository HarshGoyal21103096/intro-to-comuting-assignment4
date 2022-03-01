#QUES2
from math import factorial,remainder
from tracemalloc import start
n=int(input("enter size of pascals triangle"))

print("using for loop")
for i in range(n):
    for j in range(n-i+1):
        print(end=" ") #for spacing
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")  #nCr=n!/((n-r)!*r!)
    print() #for new line
print("\n\n")

print("using while loop")
i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i)//(factorial(y)*factorial(i-y)),end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

print("using recurssions")
def pascal_triangle(n,originallength=n):
    if n==0:
        return
    pascal_triangle(n-1,originallength)
    #printing the spaces
    print(' '*(originallength-n),end='')
    #first number i always 1
    start=1
    for i in range(1,n+1):
        
        print(start,end=' ')
        #using binomial coefficient
        start = start*(n-i)//i
    print()
pascal_triangle(n)
print("\n")

    
