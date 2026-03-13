from typing import List
from bot.errors import input_error
from bot.addressbook import AddressBook, Record
from bot.notebook import Notebook
from bot.note import Note

@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise IndexError
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message

@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args[0], args[1], args[2]

    record = book.find(name)
    if record is None:
        return "Contact not found."

    # знайти телефон для заміни
    for i, phone_obj in enumerate(record.phones):
        if phone_obj.value == old_phone:
            record.phones[i] = type(phone_obj)(new_phone)  # створює новий Phone (з валідацією)
            return "Contact updated."

    return "Old phone not found."

# Returns all phones for a contact in one line separated by "; "
@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    phones = "; ".join(phone.value for phone in record.phones)
    return phones if phones else "No phones."

@input_error
def show_all(args: List[str], book: AddressBook) -> str:
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values())

@input_error
# Adds birthday to an existing contact; date must be in DD.MM.YYYY.
def add_birthday(args: List[str], book: AddressBook) -> str:
    name, bday = args[0], args[1]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_birthday(bday)
    return "Birthday added."

@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    if record.birthday is None:
        return "Birthday not set."

    return record.birthday.value.strftime("%d.%m.%Y")

@input_error
# Prints upcoming birthdays for the next week using AddressBook.get_upcoming_birthdays().
@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    days = 7

    if args:
        days = int(args[0])
        if days < 0:
            raise ValueError("Days must be a non-negative number.")

    upcoming = book.get_upcoming_birthdays(days)

    if not upcoming:
        return f"No birthdays in the next {days} days."

    lines = [f"{u['name']}: {u['congratulation_date']}" for u in upcoming]
    return "\n".join(lines)

@input_error
def add_email(args: List[str], book: AddressBook) -> str:
    # Add a new email to a contact
    name, email = args

    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_email(email)
    return "Email added."

@input_error
def remove_email(args: List[str], book: AddressBook) -> str:
    # Remove email from contact
    name, email = args[0], args[1]

    record = book.find(name)
    if record is None:
        return "Contact not found."

    found_email = record.find_email(email)

    if found_email is None:
        return "Email not found."

    record.remove_email(email)
    return "Email removed."

@input_error
def add_address(args: List[str], book: AddressBook) -> str:
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_address(address)
    return "Address added."

@input_error
def search_contacts(args: List[str], book: AddressBook) -> str:
    # Search contacts by name, phone or email
    # Supports partial case-insensitive match
    query = " ".join(args)
    results = book.search(query)

    if not results:
        return "No matching contacts found."

    return "\n".join(str(record) for record in results)


@input_error
def delete_contact(args: List[str], book: AddressBook) -> str:
    # Delete contact by name from address book
    name = args[0]
    record = book.find(name)

    if record is None:
        return "Contact not found."

    book.delete(name)
    return "Contact deleted."


@input_error
def change_email(args: List[str], book: AddressBook) -> str:
    name, old_email, new_email = args[0], args[1], args[2]

    record = book.find(name)
    if record is None:
        return "Contact not found."

    found_email = record.find_email(old_email)

    if found_email is None:
        return "Old email not found."

    found_email.value = new_email
    return "Email updated."


@input_error
def change_address(args: List[str], book: AddressBook) -> str:
    # Change or set address for a contact
    # Address may contain spaces
    name = args[0]
    new_address = " ".join(args[1:])

    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_address(new_address)
    return "Address updated."


@input_error
def change_birthday(args: List[str], book: AddressBook) -> str:
    # Change or set birthday for a contact
    # Date format must be DD.MM.YYYY
    name, new_birthday = args[0], args[1]

    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_birthday(new_birthday)
    return "Birthday updated."

@input_error
def add_note(args: List[str], notebook: Notebook) -> str:
    if len(args) < 2:
        raise IndexError
    title = args[0]
    body = " ".join(args[1:])
    note = Note(title, body)
    notebook.add(note)
    return "Note added."

@input_error
def show_notes(args: List[str], notebook: Notebook) -> str:
    if not notebook.notes:
        return "No notes found."
    lines = [f"{n.title}: {n.body}" for n in notebook.notes]
    return "\n".join(lines)

@input_error
def find_note(args: List[str], notebook: Notebook) -> str:
    query = args[0]
    results = notebook.find(query)
    if not results:
        return "No notes found."
    lines = [f"{n.title}: {n.body}" for n in results]
    return "\n".join(lines)

@input_error
def edit_note(args: List[str], notebook: Notebook) -> str:
    if len(args) < 2:
        raise IndexError
    title = args[0]
    new_body = " ".join(args[1:])
    if notebook.edit(title, new_body):
        return "Note updated."
    return "Note not found."

@input_error
def delete_note(args: List[str], notebook: Notebook) -> str:
    title = args[0]
    if notebook.delete(title):
        return "Note deleted."
    return "Note not found."

@input_error
def add_tag(args: List[str], notebook: Notebook) -> str:
    if len(args) < 2:
        raise IndexError

    title = args[0]
    tag = args[1]

    note = notebook.find_by_title(title)
    if note is None:
        return "Note not found."

    note.add_tag(tag)
    return "Tag added."


@input_error
def find_by_tag(args: List[str], notebook: Notebook) -> str:
    tag = args[0]
    results = notebook.find_by_tag(tag)

    if not results:
        return "No notes found."

    lines = []
    for note in results:
        tags = ", ".join(note.tags) if note.tags else "no tags"
        lines.append(f"{note.title}: {note.body} | tags: {tags}")

    return "\n".join(lines)


@input_error
def sort_by_tag(args: List[str], notebook: Notebook) -> str:
    tag = args[0]
    results = notebook.sort_by_tag(tag)

    if not results:
        return "No notes found."

    lines = []
    for note in results:
        tags = ", ".join(note.tags) if note.tags else "no tags"
        lines.append(f"{note.title}: {note.body} | tags: {tags}")

    return "\n".join(lines)