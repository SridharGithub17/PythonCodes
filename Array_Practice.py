#/bin/usr/python
#Array Testing practices

def SumOfArray(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    print("Sum of arracy elements : ", sum)

def FindLarge(arr):
    prev =0 
    for i in arr:
        if i > prev :
            large = i
            prev= i

    print("Large value inthe array: ", large)  

def ArrayRotation(arr, d, n):
    arr1= []
    arr2= []
    arr3= []
    i,j= 0,0
    print("Original Array Element: ", arr)
    for r in range (0 , n):
        print(arr[r])
        if r <= d:
                arr1.append(arr[r])
                #i+= 1
        else:
                arr2.append(arr[r])
                #j+= 1

    print("First Array: ", arr1)
    print("2nd Array: ", arr2)
    print("Length of array", len(arr))

    for k in range(len(arr), 0):
        arr3.append(arr[k])
        # print(arr[k])
        # k-= 1

    print("Reverse of Original Array: ", arr3 )


def main():
    #sum of array
    arr= []
    arr = [500, 34,33,44,55,100]
    # SumOfArray(arr)
    # FindLarge(arr)
    ArrayRotation(arr, 2, 6)

if __name__ == "__main__":
    main()