#/bin/usr/python
#String operations
import string
import random
import time

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
    
def PrintString():
    string = input("Enter string:  ")
    newStr =""
    for i in range(len(string)):
        if string[i]==" ":
            print (newStr+'\n')
            newStr=""
        else:
            newStr =  newStr + string[i]
    print(newStr)

import strgen
def RandomStringGenerator():
    letters = string.ascii_letters
    LCaseLetter = string.ascii_lowercase
    UCaseLetter = string.ascii_uppercase
    result_str = random.choice(letters)
    length = 8
    result_LCstr = ''.join(random.choice(LCaseLetter) for i in range(length))
    result_UCstr = ''.join(random.sample(UCaseLetter, length ))
    print("New Strings  : ", result_str, result_LCstr, result_UCstr)
    LettersDigits = string.ascii_letters + string.digits
    resultMixString = ''.join( random.sample(LettersDigits, length))
    print ("Mix String : ", resultMixString)
    ##############################
    randomString1 = strgen.StringGenerator("[\w\d]{5}").render()
    randomString2 = strgen.StringGenerator("[\d]{3}&[\w]{3}&[\p]{3}").render()
    print("New Random Strings  :", randomString1, randomString2)


def CheckAllVowels():
    string = input("Enter the string : ")
    CaseA, CaseI, CaseO, CaseE, CaseU = 0,0,0,0,0
    print("Length of string : ", len(string))
    for i in range(len(string)):
        if string[i].upper() == 'A':
            CaseA =1
        elif string[i].upper() == 'E':
               CaseE =1
        elif string[i].upper() == 'I':
               CaseI =1
        elif string[i].upper() == 'O':
               CaseO =1
        elif string[i].upper() == 'U':
               CaseU =1
        else:
            continue
    
    print(CaseA, CaseI, CaseO, CaseE, CaseU)
    if ( int(CaseA) + int(CaseE) + int(CaseI) + int(CaseO) + int(CaseU) ) == 5:
        print("All the vowels are present ")
    else:
        print("All the vowels not present ")

def ExecuteCode():
    LOC ="""
def prints():
    return "sridhar"
print(prints())
print("sridhar das")
         """
    
    exec(LOC)

def main():
    ExecuteCode()
    # CheckAllVowels()
    # PalindromeCheck()
    # ReverseString()
    # RemoveCharString()
    # CheckSubString()
    # WordCount()
    # TitleReplace()
    # PrintString()
    # RandomStringGenerator()

if __name__ == "__main__":
    main()