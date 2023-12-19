from rich.console import Console as RichConsole
from rich.theme import Theme


custom_theme = Theme({
    'success': 'green',
    'error': 'red',
})

console = RichConsole()


class Console:
    @staticmethod
    def print(text: str):
        console.print(text)

    @staticmethod
    def print_error(text: str):
        console.print(text, style='bold red')

    @staticmethod
    def print_success(text: str):
        console.print(text, style='success')
