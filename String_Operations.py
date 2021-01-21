#/bin/usr/python
#String operations

def PalindromeCheck():
    string = input("Enter value of string:  ")
    j= len(string)-1
    for i in range(0,len(string)):
        if string[i] == string[j]: 
            i+= 1
            j-= 1
            if i == j:
                print("String is a Palindrome")
                exit()
            else:
                continue
        else:
            print("String is not Palindrome")
            exit()
    
def ReverseString():
    Rstr =""
    string = input("Enter value of String : ")
    Len,i = len(string), len(string)-1
    print("Length of String :", Len)
    while i >= 0:       
        Rstr= Rstr + string[i]
        i-= 1
    print("Reverse String: ", Rstr)

def RemoveCharString():
    Rstr=""
    string = input("Enter String :")
    n = input("Nth char to remove from string: ")
    # i = len(string)-1
    for i in range(len(string)-1):
        if i != n: 
            Rstr= Rstr + string[i]
    print("Final string: ", Rstr )   

def CheckSubString():
    string = input("Enter String : ")
    SubString = input("Enter Sub String : ")
    NewStr=""
    StrLen, SubStrLen = len(string), len(SubString)
    i,j=0,0
    if StrLen == SubStrLen:
        if string == SubString:
            print("String is same as substring")
        else:
            print("Substring is not same as string")
    elif  StrLen < SubStrLen:
            print("Substring cant be part of string")
    else:
        while i <= StrLen-1:
            j=i
            while j <= i+ ( SubStrLen-1):
                NewStr = NewStr + string[j]
                j+= 1
            print("New String", NewStr)
            if NewStr == SubString:
                print("Substring is present")
                exit()
            NewStr=""
            i+= 1

def WordCount():
    string = input("Enter String : ")
    SubString = input("Enter Sub String : ")
    NewStr=""
    StrLen, SubStrLen = len(string), len(SubString)
    i,j, count =0,0,0
    if StrLen == SubStrLen:
        if string == SubString:
            print("String is same as substring")
        else:
            print("Substring is not same as string")
    elif  StrLen < SubStrLen:
            print("Substring cant be part of string")
    else:
        while i <= StrLen-1:
            j=i
            while j <= i+ ( SubStrLen-1):
                    NewStr = NewStr + string[j]
                    j+= 1
            print("New String", NewStr)
            if NewStr == SubString:
                print("Substring is present")
                count+= 1
            NewStr=""
            i+= 1
            if i+ (SubStrLen-1) >= StrLen:
                    print("Word "+ SubString + " is present : "+ str(count) + " times ")
                    exit()

def TitleReplace():
    string = input("Input string with special charecters : ")
    NewStr =""
    for i in range(len(string)-1):
        if (not string[i].isalnum()):
            NewStr= NewStr+ string[i]
        else:
            NewStr= NewStr + string[i].replace(string[i],"") 
    print("Final string without special charecter : ", NewStr)
    

def main():
    # PalindromeCheck()
    # ReverseString()
    # RemoveCharString()
    # CheckSubString()
    # WordCount()
    TitleReplace()

if __name__ == "__main__":
    main()