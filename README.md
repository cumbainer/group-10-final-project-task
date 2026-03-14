# Personal Assistant Bot

CLI-бот для керування контактами та нотатками.

## Встановлення

```bash
git clone https://github.com/cumbainer/group-10-final-project-task.git
cd group-10-final-project-task
pip install .
```

## Запуск

```bash
assistant-bot
```

Або без встановлення:

```bash
python -m bot.cli
```

## Команди

### Контакти

| Команда | Опис |
|---------|------|
| `add <name> <phone>` | Додати контакт |
| `change <name> <old_phone> <new_phone>` | Змінити телефон |
| `phone <name>` | Показати телефони |
| `all` | Показати всі контакти |
| `search <query>` | Пошук за ім'ям, телефоном або email |
| `delete <name>` | Видалити контакт |
| `add-email <name> <email>` | Додати email |
| `change-email <name> <old_email> <new_email>` | Змінити email |
| `remove-email <name> <email>` | Видалити email |
| `add-address <name> <address>` | Додати адресу |
| `change-address <name> <new_address>` | Змінити адресу |
| `add-birthday <name> <DD.MM.YYYY>` | Додати день народження |
| `change-birthday <name> <DD.MM.YYYY>` | Змінити день народження |
| `show-birthday <name>` | Показати день народження |
| `birthdays [days]` | Найближчі дні народження (за замовчуванням 7 днів) |

### Нотатки

| Команда | Опис |
|---------|------|
| `add-note <title> <text...>` | Додати нотатку |
| `show-notes` | Показати всі нотатки |
| `find-note <text>` | Знайти нотатку за текстом |
| `edit-note <title> <new_text...>` | Редагувати нотатку |
| `delete-note <title>` | Видалити нотатку |

### Теги

| Команда | Опис |
|---------|------|
| `add-tag <title> <tag>` | Додати тег до нотатки |
| `find-by-tag <tag>` | Знайти нотатки за тегом |
| `sort-by-tag <tag>` | Сортувати нотатки за тегом |

### Загальні

| Команда | Опис |
|---------|------|
| `hello` | Привітання |
| `help` | Список всіх команд |
| `close` / `exit` | Зберегти та вийти |

## Приклад використання

```
$ assistant-bot

> add Alice 1234567890
Contact added.
> add-email Alice alice@example.com
Email added.
> add-birthday Alice 15.06.1990
Birthday added.
> add-note Shopping buy milk and bread
Note added.
> add-tag Shopping food
Tag added.
> find-by-tag food
Shopping: buy milk and bread | tags: food
> close
Good bye!
```

## Збереження даних

Дані зберігаються автоматично при виході (`close` / `exit`) у файли `addressbook.pkl` та `notebook.pkl` через pickle-серіалізацію. При наступному запуску дані завантажуються автоматично.

## Структура проєкту

```
bot/
    __init__.py
    addressbook.py    — моделі даних (Field, Name, Phone, Email, Address, Birthday, Record, AddressBook)
    commands.py        — обробники команд з @input_error декоратором
    cli.py             — точка входу, маршрутизація команд через словники
    errors.py          — декоратор обробки помилок
    note.py            — клас Note
    notebook.py        — клас Notebook
    storage.py         — pickle save/load
    welcome_help.py    — меню привітання та help
pyproject.toml         — конфігурація пакету (pip install .)
```

## Технології

- Python 3.10+
- ООП (ієрархія класів Field → Name, Phone, Email, Birthday, Address)
- `UserDict` як базовий клас для AddressBook
- Pickle для серіалізації даних
- Property/Setter для валідації полів
- Паттерн Декоратор для обробки помилок

## Kanban Board

https://trello.com/b/WFyvkcIR/project

## Розробники

1. Olya Harkavenko
2. Vladyslav Shtaiier
3. Borys Zhyhalo
4. Karina Kostiuk
