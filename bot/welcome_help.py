WELCOME_MESSAGE = """
╔════════════════════════════════════════════════════╗
║                 🤖 ASSISTANT BOT 🤖               ║
╚════════════════════════════════════════════════════╝

Welcome to the assistant bot!

✨ What this bot can do:

CONTACTS
• add new contacts
• change phone numbers
• add and edit email, address, birthday
• search contacts by name / phone / email
• delete contacts
• show one contact phone
• show all contacts
• show upcoming birthdays

NOTES
• add notes
• show all notes
• find notes by text
• edit notes
• delete notes
• add tags to notes
• find notes by tag
• sort notes by tag

GENERAL
• greet you
• show help
• exit safely with saving

💡 Type 'help' to see the full command list.
"""

HELP_MESSAGE = """
╔════════════════════════════════════════════════════╗
║                    📚 HELP MENU 📚                ║
╚════════════════════════════════════════════════════╝

How to use commands:
command + arguments

CONTACT COMMANDS
add <name> <phone>
change <name> <old_phone> <new_phone>
phone <name>
all
search <query>
delete <name>

add-email <name> <email>
change-email <name> <old_email> <new_email>
remove-email <name> <email>

add-address <name> <address>
change-address <name> <new_address>

add-birthday <name> <DD.MM.YYYY>
change-birthday <name> <DD.MM.YYYY>
show-birthday <name>
birthdays

NOTE COMMANDS
add-note
show-notes
find-note <text>
edit-note
delete-note
add-tag
find-by-tag <tag>
sort-by-tag

GENERAL COMMANDS
hello
help
close
exit
"""