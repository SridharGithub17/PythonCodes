#/bin/usr/python
#List Questions
from collections import deque
import time
#Practice more on List/tuple/set/dictionary

def ListOperations(stack, i, j):
    print("Original List", stack)
    stack.pop()
    print(stack)
    stack.append(40)
    length=len(stack)
    number= stack[j]
    stack[j] = stack[i]
    stack[i]= number
    print(stack)
    # #n = input("Number to look for: ")
    # for i in stack:
    #     if i == int(n) :
    #         print("Number exist")
    ReverseStack= []
    length = len(stack)-1
    for i in range( length ,0):
        print(stack[i])
        ReverseStack.append(stack[i])
        
    print("Reverse Stack : ", ReverseStack )
    print("Reverse using function: ", stack.reverse())

    index= stack.index(35)
    stack.remove(40)
    print(stack , index )

def Operations(stack):
    String1=[]
    for string in stack:
        if string.isdigit():
            String1.append(str(int(string) +6))
        else:
            String1.append(str(string))
    print("Updated Stack : ", String1)

def SumOfDigits(stack):
    sum= 0
    for string in stack:
        if string.isdigit():
            sum=sum+ int(string)
    print("Sum of values: ", sum)

def CumilativeSum(stack):
    sumArray = []
    sum=0
    for string in stack:
        prev= string
        sum= sum + prev
        sumArray.append(sum )

    print("Original  stack: ", stack)
    print("Cumilative Sum: ", sumArray)

def FindDuplicates(stack):
    prev=0
    duplicates = []
    count=1  #   stack = [234, 98, 123, 4,45,3,3,4,5,6]
    for string in stack:
        n= count
        print("length: ", len(stack))  
        print(string, stack[n])  
        time.sleep(5)
        while n <= len(stack)-1:
            inserted =1 
            if string == int(stack[n]) :
                # time.sleep(5)
                if inserted > 1:
                    continue
                else:
                    duplicates.append(string)
                    prev= stack[n]
                    inserted += 1
            else:
                prev= stack[n]
                continue
        count+= 1
    print("Duplicates : ", duplicates)

def PrintOddEven(stack):
    for string in stack:
        if string%2 == 0:
            print(string, "Even")
        else:
            print(string,"Odd")
    for n in range(10):
        if n%2 == 0:
            print(n, "Even")
        else:
            print(n, "Odd")

def FindLargestSmallest(stack):
    large =0#    stack = [234, 98, 123, 4,45,3,3,4,5,6]
    for string in stack:
        if string > large:
            large= string
        else:
            continue
    small= stack[0]
    for string in stack:
        if string < small:
            small=string
        else:
            continue
    print("Large number :", large)
    print("Small number : ", small)

def main():
    # stack = [12, 35,'das' ,9, 56, 24,'hari'] 
    # ListOperations(stack,2,3 )
    stack = ["gfg", "234", "is", "98", "123", "best", "4"]
    # Operations(stack)
    # SumOfDigits(stack)
    stack = [234, 98, 123, 4,45,3,3,4,5,6]
    # CumilativeSum(stack)
    # FindDuplicates(stack) --Check it more
    # PrintOddEven(stack)
    FindLargestSmallest(stack)


if __name__ == "__main__":
    main()