#/bin/usr python
import yaml
import json

def Yaml_test():    
    
    names_yaml = """
    - 'eric'
    - 'justin'
    - 'mary-kate'
    """
    try:
       
       names = yaml.safe_load(names_yaml)
       print(names)
       with open('names.yaml', 'w') as file:
            yaml.dump(names, file)

       print(open('names.yaml').read())
       
       with open('Config.yaml', 'r') as file:
         prime_services = yaml.safe_load_all(file)

         for prime_service in prime_services:
            print(prime_service)

         with open('Config.json', 'w') as json_file:
            json.dump(prime_service, json_file)

    except ZeroDivisionError: 
        print('There is some issue in the try block')
    else:
        print("In the else block")
    finally:
        print("Other errors, need diagnosis")


def main():
    Yaml_test()

if __name__ == "__main__":
    main()





