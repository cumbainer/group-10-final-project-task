import re
from collections import UserDict
from datetime import datetime, date, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        value = str(value).strip()
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        new_value = str(new_value)
        if not new_value.isdigit():
            raise ValueError("Phone must contain only digits")
        if len(new_value) != 10:
            raise ValueError("Phone must be 10 digits")
        self._value = new_value

class Email(Field):
    @Field.value.setter
    def value(self, new_value):
        new_value = new_value.strip().lower()
        if not re.match(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", new_value):
            raise ValueError("Invalid email format.")
        self._value = new_value
        

class Address(Field):
    @Field.value.setter
    def value(self, new_value):
        if not str(new_value).strip():
            raise ValueError("Address cannot be empty.")
        self._value = str(new_value).strip()


class Birthday(Field):
    def __init__(self, value: str):
        try:
            bday = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(bday)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        # Extended contact model:
        # contact can now store multiple email addresses
        self.emails = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone: str) -> None:
        # Adds a new phone to contact
        # Prevents duplicate phone numbers
        if any(p.value == phone for p in self.phones):
            raise ValueError("Phone already exists.")

        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone is not None:
            self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone:
            found_phone.value = new_phone

    def add_email(self, email: str) -> None:
        # Adds a new email to contact
        # Prevents duplicate emails
        if any(e.value == email for e in self.emails):
            raise ValueError("Email already exists.")

        self.emails.append(Email(email))

    def find_email(self, email):
        # Search email in contact email list
         for item in self.emails:
            if item.value == email:
                return item

    def remove_email(self, email):
        # Remove email from contact
        found_email = self.find_email(email)
        if found_email:
            self.emails.remove(found_email)
    
    def add_address(self, address: str) -> None:
        self.address = Address(address)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self):
        parts = [f"Contact name: {self.name.value}"]
        parts.append(f"phones: {'; '.join(p.value for p in self.phones)}")
        if self.emails:
            # Show all contact emails separated by ";"
            parts.append(f"email: {'; '.join(e.value for e in self.emails)}")
        if self.address:
            parts.append(f"address: {self.address.value}")
        if self.birthday:
            parts.append(f"birthday: {self.birthday.value.strftime('%d.%m.%Y')}")
        return ", ".join(parts)

# Helpers for upcoming birthday calculation: move weekend greetings to Monday and pick next birthday date.
def adjust_if_weekend(d: date) -> date:
    if d.weekday() == 5:
        return d + timedelta(days=2)
    if d.weekday() == 6:
        return d + timedelta(days=1)
    return d

def get_next_birthday_this_or_next_year(birthday: date, today: date) -> date:
    try:
        next_bday = birthday.replace(year=today.year)
    except ValueError:
        next_bday = date(today.year, 2, 28)
    if next_bday < today:
        try:
            next_bday = birthday.replace(year=today.year + 1)
        except ValueError:
            next_bday = date(today.year + 1, 2, 28)
    return next_bday

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def search(self, query):
        # Search contacts by name, phone or email
        # Partial match, case-insensitive
        query = query.lower()
        results = []

        for record in self.data.values():
            name_match = query in record.name.value.lower()
            phone_match = any(query in phone.value.lower() for phone in record.phones)
            email_match = any(query in email.value.lower() for email in record.emails)

            if name_match or phone_match or email_match:
                results.append(record)

        return results

    def get_upcoming_birthdays(self, days: int = 7) -> list:
        today = datetime.today().date()
        result = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday_date = record.birthday.value  # date
            next_bday = get_next_birthday_this_or_next_year(birthday_date, today)

            days_diff = (next_bday - today).days
            if not (0 <= days_diff <= days):
                continue

            congratulation_date = adjust_if_weekend(next_bday)
            result.append({
                "name": record.name.value,
                "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
            })

        return result
        


