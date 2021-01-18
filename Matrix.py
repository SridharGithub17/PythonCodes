#/bin/usr/python
#Test Matrix in python

def Operations():
    X = [[1,2,3], 
        [4 ,5,6], 
        [7 ,8,9]] 
    
    Y = [[9,8,7], 
        [6,5,4], 
        [3,2,1]]

    result = [[0,0,0], 
        [0,0,0], 
        [0,0,0]] 
  
    # iterate through rows 
    for i in range(len(X)):    
    # iterate through columns 
        for j in range(len(X[0])): 
            result[i][j] = X[i][j] - Y[i][j] 
    
    for r in result: 
        print(r)

def Transpose():
    m = [[1,2],[3,4],[5,6]]
    trans = [[0,0,0], 
             [0,0,0]]
    item, subItem=0,0
    for item in range(len(m)-1):
        for subItem in range(len(m[item])-1):
            trans[item][subItem]= m[subItem]

    print("Transposed list: ", trans)
    
def main():
    # Operations()
    Transpose()

if __name__ == "__main__":
    main()