#/bin/usr/env python

#Scopes
#4 nested scopes whose namespaces are directly accessible:
#the innermost scope, which is searched first, contains the local names
#the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
#the next-to-last scope contains the current module’s global names
#the outermost scope (searched last) is the namespace containing built-in names

def main():
    print("In the main block")





if __name__ == "__main__":
    main()