from rich.console import Console
from rich.panel import Panel

console = Console()

def show_welcome_menu():
    content = """[bold green]add <name> <phone>[/bold green]
[white]Save a new contact[/white]

[bold green]add-birthday <name> <DD.MM.YYYY>[/bold green]
[white]Save birthday[/white]

[bold green]all[/bold green]
[white]Show all contacts[/white]

[bold green]search <text>[/bold green]
[white]Find contact[/white]

[bold green]delete <name>[/bold green]
[white]Delete contact[/white]

[bold yellow]change-email <name> <email>[/bold yellow]
[bold yellow]change-address <name> <address>[/bold yellow]
[bold yellow]change-birthday <name> <date>[/bold yellow]

[bold magenta]help[/bold magenta]
[white]Show full commands table[/white]

[bold red]exit / close[/bold red]"""

    panel = Panel(
        content,
        title="[bold cyan]WELCOME TO ASSISTANT BOT[/bold cyan]",
        border_style="green",
        expand=False
    )

    console.print(panel)