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
    contacts.update({name:phone})
        
def add(name, phone):
    print(f"I add contact for <{name}> with phone <{phone}>")
    contacts.update({name:phone})

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

dict_of_operation = {
    hello:"hello",
    add:"add",
    show_all: "show all",
    phone:"phone",
    change:"change",
}


@input_error
def main():
    while True:
        user_input = input("> ").strip().strip()
        for key, val in dict_of_operation.items():
            if val in user_input:
                if int(user_input[2].isdigit()):
                    number = user_input[2]
                    name = user_input[1]
                    print(key(name, number))
                elif val == "show all":
                    print(key())
                elif val == "hello":
                    print(key())
                elif val == "phone":
                    number = user_input[1]
                    print(key(number))
                else:
                    print("Give me a name and phone please")
            elif val not in user_input:
                pass
            else:            
                print("Invalid command")
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye")
            break
        
        
if __name__ == "__main__":
    main()