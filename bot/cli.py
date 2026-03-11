from typing import Callable, Dict, List, Tuple
from bot.commands import add_contact, change_contact, show_phone, show_all
from bot.commands import add_birthday, show_birthday, birthdays
from bot.commands import add_email, add_address
from bot.commands import search_contacts, delete_contact, change_birthday, change_email, change_address
from bot.addressbook import AddressBook
from bot.storage import save_data, load_data


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Split user input into command and arguments."""
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def main() -> None:
    """Run the CLI assistant bot."""
    book = load_data()

    contact_commands: Dict[str, Callable] = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
        "add-email": add_email,
        "add-address": add_address,
        "search": search_contacts,
        "delete": delete_contact,
        "change-birthday": change_birthday,
        "change-email": change_email,
        "change-address": change_address,
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        command, args = parse_input(user_input)

        if command in {"close", "exit"}:
            save_data(book)
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        if command in contact_commands:
            print(contact_commands[command](args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
