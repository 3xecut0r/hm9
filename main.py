import re

contacts = {}

def hello():
    print("How can I help you?")

def show_all():
    if contacts == {}:
        print("List contain <0> contacts")
    else:
        for key, value in contacts.items():
            print(f"{key}: {value}")
            l=0
            l +=1
        print(f"List contain <{l}> contacts")
        
def change(name, phone):
    return contacts.update({name:phone})
        
def add(name, phone):
    print(f"I add contact for <{name}> with phone <{phone}>")
    return contacts.update({name:phone})

def phone(name):
    for k,v in contacts.items():
        if name == k:
            print(v)

def input_error(func):
    def wrapper():
        try:
            return func()
        except KeyError:
            print("There is no contact with that name")
            return func()
        except ValueError:
            print("Number is incorrect")
            return func()
        except IndexError:
            print("Give me a name and phone please")
            return func()
        
    return wrapper
            
commands = ["hello", "show all", "add", "good bye", "close", "exit", "change", "phone"]

                
@input_error
def main():
    while True:
        command = input(">>> ")
        words = re.split(r"(\W+)", command)

        if "show all" in command:
            show_all()
        
        elif "hello" in command:
            hello()
        
        elif "add" in command:
            res = command[4:].strip().split()
            if len(res)<1:
                print("Invalid command")
                continue
            add(res[0], res[1])
            
        elif command == ".":
            break
        
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        
        elif "change" in command:
            res = command[7:].strip().split()
            if 2>len(res)>0:
                change(res[0], res[1])
            else:
                print("Invalid command")
                continue
            
            
        elif "phone" in command:
            name = command[6:].split()
            if 2>len(name)>0:
                phone(name)
            else:
                print("Invalid command")
                continue
            
            
            

if __name__ == "__main__":
    main()




