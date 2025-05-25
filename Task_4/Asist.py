def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#Додавання контакту в словник
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#Оновлення номеру
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

#Пошук номеру через ім'я
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        return "Contact not found."

#Список всіх контактів
def list_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

#Список команд для допомоги користувачу
command_list = (
    "Command list:\n"
    "Add (username) (phone) - adds a contact;\n"
    "Phone (username) - searches for a phone number by username;\n"
    "Change (username) (phone) - stores the new phone number for username in memory;\n"
    "All - shows all contacts;\n"
    "Close, exit - finishes the work;"
    )
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        elif command in ["help", "command"]:
            print(command_list)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
