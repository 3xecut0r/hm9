
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

def hello(*args):
    return "How can I help you?"

def add(*args):
    pass

def phone(*args):
    pass

def change(*args):
    pass

def show_all(*args):
    return "\n".join([f"{k}:{v}" for k, v in contacts.items()])

def exit(*args):
    return "Good bye"

def unknown_command(*args):
    return "Invalid command"

COMMANDS = {
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
    user_input = input("Enter command: ")
    user_input = handler(user_input)
    
    
if __name__ == "__main__":
    main()