import re

COMMANDS = {
    hello:"hello",
    add:"add",
    phone:"phone",
    change:"change",
    show_all:"show all"
}
commands = ["hello", 'add', 'phone', 'change', 'show all']
arguments = {}


def input_error(func):
    def wrapper(*args):
        try:
            if len(args)==1:
                return func(args[0])
            elif len(args) == 0:
                return func()
            elif len(args) == 2:
                return func(args[0], args[1])
        except ValueError:
            print("Number is incorrect")
        except KeyError:
            print("There is no contact with that name")
        except IndexError:
            print("Give me a name and phone please")
    return wrapper


@input_error
def hello():
    print("How can I help you?")


@input_error
def add(*args):
    name = args[0]
    number = args[1]
    arguments.update({name:number})
    print(f"Added <{name}> : <{number}>")

@input_error
def change(*args):
    name = args[0]
    number = args[1]
    arguments.update({name:number})
    print(f"Changed <{name}> : <{number}>")

 
@input_error        
def phone(*args):
    name = args[0]
    for key, value in arguments.items():
        if name == key:
            print(value)

@input_error
def show_all():
    print(arguments)
    
    
def handler(string):
    string = string.lower()
    command = ""
    for item in commands:
        match = re.findall(item, string)
        if len(match)>0:
            command = item
            break
        
    result = []
    
    if command == "hello":
        return hello()
    
    elif command == "show all":
        return show_all()
    
    else:
        active = False
        for i in string.split():
            if active:
                result.append(i)
            elif i == command:
                active = True
                result.append(i)
        return result

@input_error
def main():
    while True:
        user_input = input('Enter command: ')
        user_input = handler(user_input)
        
        if "exit" in user_input:
            print("Good bye")
            break
        
        elif user_input[0] == "add":
            add([user_input[1], user_input[2]])
            
        elif user_input[0] == "change":
            change([user_input[1], user_input[2]])
            
        elif user_input[0] == "phone":
            phone([user_input[1]])
        
        
if __name__ == "__main__":
    main()
