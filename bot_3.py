
contacts = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError:
            return "Number is incorrect"
        except KeyError:
            return "There is no contact with that name"
        except IndexError:
            return "Give me a name and phone please"
    return wrapper

def help(*args):
    return """
help: To see this message
add <Name> <phone>: add
change <Name> <phone>: change contact's name of phone
show all: List of contacts
hello: hello
phone <Name>: To see phone number of <Name>
exit: If you want to exit
"""

@input_error
def hello(*args):
    return "How can I help you?"

@input_error
def add(*args):
    command = args[0].split()
    name = command[0]
    number = command[1]
    contacts.update({name:phone})
    return f"Added <{name}> with phone <{number}>"

@input_error
def phone(*args):
    name = args[0]
    return contacts[name]

@input_error
def change(*args):
    command = args[0].split()
    name = command[0]
    number = command[1]
    contacts.update({name:number})
    return f"Changed <{name}>:<{number}>"

@input_error
def show_all(*args):
    return "\n".join([f"{k}:{v}" for k, v in contacts.items()])

@input_error
def exit(*args):
    return "Good bye"

@input_error
def unknown_command(*args):
    return "Invalid command"

COMMANDS = {
    help:"help",
    hello:"hello",
    add:"add",
    phone:"phone",
    change:"change",
    show_all:"show all",
    exit:"exit"
}

def handler(string):
    for key, value in COMMANDS.items():
        if string.startswith(value):
            return key, string.replace(value, "").strip()
    return unknown_command, None

def main():
    while True:
        user_input = input("Enter command: ")
        command, data = handler(user_input)
        print(command(data))
        if command == exit:
            break
        

        
    
    
if __name__ == "__main__":
    main()