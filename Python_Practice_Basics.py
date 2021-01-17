#!/usr/bin/python

def add(a,b):
    return int(a)+int(b)

def max(a,b):
    if (a > b) :
        return a
    else:    
        return b
    
def factorial( a):
    fact=1
    if a ==0:
        print("Factorial value is: 0 ")
    elif int(a) ==1:
            print("Factorial value is :1")
    else:
        while int(a) >= 1:
            fact = fact*int(a)
            a= int(a)-1
    print ("Factorial of a number is : {0}".format(fact))

def CalcSimpleInterest( a, b, c):
    return (float(a)+ int(b)+float(c)/100)

def CalcCompoundInterest( a, b, c):
    Amount = float(a) * (pow((1 + float(b) / 100), int(c))) 
    CI = Amount - float(a) 
    return CI
#Check it one more time
def ArmstrongNumberCheck(n):
    if int(n) < 0 :
        print("Its not an Armstrong Number")
    else:
        NumOfDigits = len(n)
        print("Number of Digits in the number: ", NumOfDigits)
        i, j, FString=0,0,0
        while i < int(NumOfDigits):
            string1=1
            while j <  int(NumOfDigits):
                string1= int(string1) * int(n[i])
                j=int(j)+1
            print(n[i])
            i= int(i)+1
            FString = int(FString) + int(string1)
            print("Value of string1:", string1, FString)

        print("Value of final String:",FString)
        if FString == int(n):
            print("Number is an Armstrong Number")
        else:
            print("Number is not an Armstrong Number")

def CalcArea(R):
    pi=3.142
    print("Area of Square: %.5f", pi*float (R)* float(R))

def PrintPrime(R1,R2):
    for i in range(int(R1),int(R2)):
        if i>1:
          for j in range(2,i):
                if(i%j == 0):
                    break
                else:
                    print("Number is prime")

def FindFibonacci( n):
    a, b='0','1'
    string = a +' '+ b
    print(string)
    if n == 0:
        print("Fibonacci numbers are : ", n )
    elif n == 1:
        print("Fibanacci numbers are : ",n)
    else:
        for i in range(2, int(n)):
            c = a + b 
            a = b 
            b = c 

    print("Fibonacci numbers are :", c )

def FindAsciiValue(n):
    print("Ascii value of n is ", ord(n))

def CalcSumOfSquares( n):
    i, sum=0,0
    if n==0 :
        print("Sum of squares :  ", n)
    elif n==1:
        print("Sum of squares: ", n)
    else:
        while i <= int(n):
            sum = int(sum) + ( i * i)
            print(sum)
            i=i+1
                
    print("SUM OF VALUES ARE:", sum)

def CalcCubeOfNumbers(n):
    i, sum=0,0
    if n==0 :
        print("Sum of squares :  ", n)
    elif n==1:
        print("Sum of squares: ", n)
    else:
        while i <= int(n):
            sum = int(sum) + ( i * i * i)
            i=i+1
                
    print("SUM OF VALUES ARE:", sum)

def main():
    #add 2 numbers from input
    """ a= input("Input Value for a")
    b= input("Input value for b")
    sum=add(a,b)
    print("Addition of 2 numbers {0} {1} is : {2}" .format(a,b, sum)) """
    
    #Max of 2 numbers
    # a= input("Input Value for a")
    # b= input("Input value for b")
    # maxval= max(a,b)
    # print("Max value between {0} and {1} is : {2} ".format(a,b,maxval ))
    #Program to get factorial of a number
    #factorial(a)
    # Amount = input("Input Value for Amount")
    # Years = input("Input value for Years")
    # Rate = input("Input value for Rate")
    # InterestAmount=CalcSimpleInterest(Amount, Years, Rate)
    # print("Simple Interest Amount is : {0}".format(InterestAmount))
    # CompoundInterestAmount =CalcCompoundInterest(Amount, Years, Rate)
    # print("Compound Interest Amount is: {0}".format(CompoundInterestAmount))
    #Armstrong Number Check
    #n=input("Value for n")
    #ArmstrongNumberCheck(n)
    #Area of circle
    # Radius=input("Value for Radius")
    # CalcArea(Radius)
    # range1=input("Enter Range1")
    # range2=input("Enter Range2")
    # PrintPrime(range1,range2)
    n=input("Enter input value for n:  ")
    # FindFibonacci(n)
    # FindAsciiValue(n)
    # CalcSumOfSquares( n)
    CalcCubeOfNumbers(n)


if __name__ == "__main__":
    main()