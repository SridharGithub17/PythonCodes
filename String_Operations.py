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
    

def main():
    PalindromeCheck()


if __name__ == "__main__":
    main()