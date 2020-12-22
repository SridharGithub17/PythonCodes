#/usr/bin/env/python

import PKG
from PKG import BooleanFunctions, MathFunctions
from PKG.SUB_PKG import ScintificDerivations

def main():
    try:
        resultB= PKG.BooleanFunctions.Binary(10)
        print(resultB)
        resultM = PKG.MathFunctions.add(4,5)
        print(resultM)
        resultCos = PKG.SUB_PKG.ScintificDerivations.get_cos(40)
        resultSin = PKG.SUB_PKG.ScintificDerivations.get_sin(40)
        print(str(resultSin)  + '  :  '+ str(resultCos))
    
    except ImportError:
        print("There is an error in Import")

if __name__ == "__main__":
  main()