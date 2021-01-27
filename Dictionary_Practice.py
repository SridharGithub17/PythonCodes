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

def DictSorting(dict1, dict2):
    print(sorted(dict1,key=itemgetter()), dict2 )

def MergeDict(lis1, lis2):
    # print(lis1, lis2)
    print(lis1.update(lis2))

def DictFlattening(dict1):
    dict2={}
    list1=[]
    list2=[]
    for key, value in dict1.items():
        if key == 'name':
            list1=value
        else:
            list2=value
    for i in range(len(list1)):
        dict2[list2[i]] = list1[i]
        # dict2[list1[i]]= list2[i]
    print("New Dictionary : ", dict2)

from collections import OrderedDict

def DictOps(dict1):
    print(dict1)
    dict1.update({6:'June'})
    print(dict1)
    dict1.update({7:'July'})
    dict1.move_to_end(7, last= False)
    print(dict1)

def FindWinner(votes):
    print(votes)
    count, large = 0, 0
    dictWinner = {}
    for i in range(len(votes)):
        # print(vote[i])
        for j in range(len(votes)):
            if votes[i] == votes[j]:
                count+= 1
            else:
                continue
        dictWinner[votes[i]] = count 
        count=0
    print("Final Dictionary: ", dictWinner)
    Winner, WinnerVoteCount  = 0, 0
    for key, val in dictWinner.items():
        if val >= WinnerVoteCount:
            Winner = key 
            WinnerVoteCount = val
        else:
            continue
    print('Winner in the vote is {0} with vote count {1}'.format(Winner, WinnerVoteCount))


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
    lis1 = [{ "name" : "Nandini", "age" : 20},  
            { "name" : "Manjeet", "age" : 50 }, 
            { "name" : "Nikhil" , "age" : 19 }]
    lis2 = [{ "name" : "Hari", "age" : 30},  
            { "name" : "Ranga", "age" : 100 }, 
            { "name" : "Rus" , "age" : 190 }]
    # DictSorting(lis)
    # MergeDict(dict1, dict2)
    DictOrig={'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]}
    # Expected  OUtput: Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}
    # DictFlattening(DictOrig)
    dict1= OrderedDict({1: 'Jan', 2: 'Feb', 3: 'March', 4: 'April'})
    # DictOps(dict1)
    votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]
    FindWinner(votes)

if __name__ == "__main__":
    main()