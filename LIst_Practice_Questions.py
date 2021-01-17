#/bin/usr/python
#List Questions
from collections import deque

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


def main():
    # stack = [12, 35,'das' ,9, 56, 24,'hari'] 
    # ListOperations(stack,2,3 )
    stack = ["gfg", "234", "is", "98", "123", "best", "4"]
    Operations(stack)

if __name__ == "__main__":
    main()