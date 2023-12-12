#/bin/usr python
import numpy as np

def NumPy_Test():    
    try:
        a=np.array([1, 2, 3], dtype=complex)
        print(a)

        print(a[0])

    except ZeroDivisionError: 
        print('There is some issue in the try block')
    else:
        print("In the else block")
    finally:
        print("Other errors, need diagnosis")


def main():
    NumPy_Test()

if __name__ == "__main__":
    main()