#/bin/usr/env python

def main():
    try:
        print("Sridhar is a good guy")
        x=10
        y=0
        print("z =: "+  str(x/y))
        

    except ZeroDivisionError: 
        print('There is some issue in the try block')
    else:
        print("In the else block")
    finally:
        print("Other errors, need diagnosis")

if __name__ == "__main__":
  main()