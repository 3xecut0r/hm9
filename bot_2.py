commands = ['add', 'phone', 'change', 'show all']
arguments = {}

def add(name, phone):
    arguments.update({name:phone})
    print(f"Added <{name}> with number <{phone}>")

def change(name, phone):
    try:
        arguments.update({name:phone})
    except:
        print("There is no contact with that name")
        
def phone(name):
    for key, value in arguments.items():
        if name == key:
            print(value)

def show_all():
    print(arguments)
    
def input_error(func):
    def wrapper():
        try:
            func()
        except ValueError:
            print("Number is incorrect")
            func()
        except KeyError:
            print("There is no contact with that name")
            func()
        except IndexError:
            print("Give me a name and phone please")
            func()
    return wrapper


@input_error
def main():
    while True:
        user_input = input('Enter command: ').split()
        
        for i in range(1, len(user_input)):
            if i+1 < len(user_input):
                arguments[user_input[i]] = user_input[i+1]
                print(arguments)
            elif len(user_input)>2:
                print("Invalid command")
        if user_input[0] == 'add':
            name = user_input[1]
            number = user_input[2]
            add(name, number)
        elif user_input[0] == 'phone':
            name = user_input[1]
            phone(name)
        elif user_input[0] == 'change':
            name = user_input[1]
            number = user_input[2]
            change(name, number)
        elif user_input[0] == 'hello':
            print("How can I help you?")
        elif user_input[0] + " " + user_input[1] == 'show all':
            show_all()
        elif user_input[0] + " " + user_input[1] == "Good bye":
            print("Good bye")
            break
        elif user_input[0] == "exit" or "close":
            print("Good bye")
            break
        else:
            print("Invalid command")
        
        
if __name__ == "__main__":
    main()


