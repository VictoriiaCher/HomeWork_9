from time import sleep


def input_error(func):
    def wrapper(user_data):
        try:
            return func(user_data)
        except KeyError:
            msg = "Contact is not found. Try again!"
            return msg
        except ValueError:
            msg = "You didn't enter the phone number. Try again!"
            return msg
        except IndexError:
            msg = "You didn't enter the contact name or phone. Try again!"
            return msg

    return wrapper


@input_error
def handler(command: str):
    return HANDLER[command]


def main():
    user_input = input("For start say 'hello': ").lower()

    while True:
        command, user_data = handle_user_input(user_input)
        try:
            output = handler(command)(user_data)
        except TypeError:
            print(f"I dont understand the command '{command}'. Try again!")
        else:
            print(output)
        user_input = input("\n" + "How can i help you?: ").lower()


@input_error
def handle_user_input(user_input: str) -> list:
    "Функція 'розпізнає' команду та інформацію про контакт"

    data = user_input.split()
    if data[0] in ("add", "change", "phone", "del"):
        command, user_data = data[0], data[1:]
    else:
        command, user_data = data[0], []
    return command, user_data


@input_error
def hello_handler(*args, **kwargs):
    first = "Hi! I'm your bot and i can: add -> (add...), change ->(change...), del -> (del...) contacts. \n"
    second = "You can see all contacts ->(show all) and phone by contact name -> (phone...).\n"
    three = "To exit, enter any of the commands -> (exit, good bye, close)."
    return first + second + three


@input_error
def add_handler(user_data: list) -> str:
    "Функція додає новий контакт у список контактів"

    name, phone = user_data[0], int(user_data[1])
    dictionary.update({name: phone})
    return f"New contact {name}: {phone} is added"


@input_error
def change_handler(user_data: list) -> str:
    "Функція зберігає новий номер телефону існуючого контакту"

    if dictionary[user_data[0]]:
        dictionary[user_data[0]] = int(user_data[1])
        return f"Contact {user_data[0]} is changed"


@input_error
def show_phone_handler(user_data: list) -> str:
    "Функція виводить на екран номер телефону існуючого контакту"

    return "%s" % dictionary.get((user_data[0]), "Contact is not found")


@input_error
def bye_handler(*args, **kwargs):
    "Закінчення діалогу"

    print("Goodbye!")
    sleep(3)
    return exit()


@input_error
def del_handler(user_data: list) -> str:
    "Функція видаляє контакт зі списку контактів"

    dictionary.pop(user_data[0])
    return f"Contact {user_data[0]} is delete"


@input_error
def show_all_handler(*args, **kwargs) -> str:
    "Функція виводить на екран весь список контактів"

    dict_to_str, count = [], 0
    for name, phone in dictionary.items():
        count += 1
        dict_to_str.append("{}. {}: {}".format(count, name, phone))
    dict_output = "\n".join(dict_to_str)

    return dict_output


dictionary = {
    "vika": "+380993382352",
    "alex": "+380660605759",
    "marina": "+380937169687",
}

HANDLER = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "show": show_all_handler,
    "del": del_handler,
    "phone": show_phone_handler,
    "exit": bye_handler,
    "close": bye_handler,
    "good": bye_handler,
}

if __name__ == "__main__":
    main()
