from rich.console import Console as RichConsole
from rich.table import Table
from random import randint
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

console = RichConsole()

table_colors = ['slate_blue1', 'magenta', 'chartreuse1', 'sea_green1', 'pale_turquoise1', 'yellow2']
input_emojis = ['🤩', '😃', '😂', '🤑', '🤗', '😜', '🤠', '🥸', '🤡', '🥳', '😍']


class Console:
    @staticmethod
    def print_error(text: str):
        console.print('🤯 ', text, style='red')

    @staticmethod
    def print_success(text: str):
        console.print('🥳 ', text, style='chartreuse1')

    @staticmethod
    def print_tip(text: str):
        console.print('🤓', text, style='wheat1')

    @staticmethod
    def input(text: str):
        return console.input(prompt=f'{input_emojis[randint(0, len(input_emojis) - 1)]} [sky_blue3]{text}[/]', markup=True, emoji=True, password=False, stream=None)

    @staticmethod
    def input_prompt(text: str, prompts: [str]):
        completer = WordCompleter(prompts)

        return prompt(f'{input_emojis[randint(0, len(input_emojis) - 1)]} {text}', completer=completer)

    @staticmethod
    def print(text: str, justify='left'):
        console.print(text, justify=justify)

    @staticmethod
    def print_table(title: str, column_titles: [str], rows: [[]]):
        table = Table(title=title)

        for index, title in enumerate(column_titles):
            table.add_column(title, style=table_colors[index], justify='center', vertical='top', min_width=15)

        for row in rows:
            table.add_row(*row)

        console.print(table, justify='center')

