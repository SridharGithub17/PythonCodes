#!/bin/usr/python
from operator import itemgetter

def DictionaryOperations(dict1):
    print("Original dictionary value: ", dict1)
    for key, val in dict1.items():
        if isinstance(val, list):
            print("Its a list")
            print( key+','+ str(val))
            NewStr =""
            for i in range(len(val)):
                NewStr = NewStr + str(val[i])
            print("New String :", NewStr)
        elif isinstance(val, tuple):
            print("Its a tuple")
            NewStr =""
            for i in range(len(val)):
                NewStr = NewStr + str(val[i])
            print("New String :", NewStr)
        elif isinstance(val, dict):
            print("its a dictionary")
            for key, val in val.items():
                print("Key : ",key,"val: ", val)
        elif isinstance(val, set ):
            print("Its a set", val)
            NewStr=""
            for s in val:
                NewStr = NewStr + str(s)
            print("New String :", NewStr)
        

def TypeCheck(dict1):
    for key, val in dict1.items():
        if isinstance(val, list):
            print("Its a list")
        elif isinstance(val, tuple):
            print("Its a tuple")
        elif isinstance(val, dict):
            print("its a dictionary", type(val))
        elif isinstance(val, set ):
            print("Its a set", type(val), val)

def DictMathOperations(dict):
    sum=0
    for key, val in dict.items():
        sum= sum + val
    print("Sum of Dict items: ", sum)
    # del dict['a']
    # dict.pop('a')
    print("Dictionary after del operation: ", dict)
    dict.update({'b':30000})
    print("Updated dictionary :", dict)

def DictSorting(lis):
    print(sorted(lis, key=itemgetter('age')))


def main():
    dict1= {'aaa': [3,3,4,4,5,5],
    'bbb': [3,3,4,4,5,6],
    'ccc': (3,3,4,4,5,7), ###tuple
    'ddd': {3,3,4,4,5,8},  ##Set
    'eee': {'a':3,'b':3,'c':4,'d':4,'e':5,'f':9} #Dictionary
    }
    dict2={'a': 100, 'b':200, 'c':300,'d':45,'e':6}
    # DictionaryOperations(dict1)
    # TypeCheck(dict1)
    # DictMathOperations(dict2)
    lis = [{ "name" : "Nandini", "age" : 20},  
            { "name" : "Manjeet", "age" : 50 }, 
            { "name" : "Nikhil" , "age" : 19 }]
    DictSorting(lis)

if __name__ == "__main__":
    main()