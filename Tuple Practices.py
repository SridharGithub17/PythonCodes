#!/bin/usr/python
#Tuple operations test
def TupleOperations(tup1):
    for ele in tup1:
        print("Elements: ", ele)
    print("Size of Tuple : ", tup1.__sizeof__())

def FlattenTuple(t):
    print("Original Tuple :", t)
    Tuple2 = t
    str1 =""
    for ele in range(len(t)):
        print("Elements :", tuple(t[ele]) )
        str1 = str1 + str(tuple(t[ele]))

    print("New Tuple after operations :", Tuple2)
    # print("New Tuple after string concat : ", tuple(str1))

def main():
    tup1=(3,3,4,4,5,'sri')
    # TupleOperations(tup1)
    tuple1 = ([5], [6], [3], [8])
    FlattenTuple(tuple1)


if __name__ == "__main__":
    main()