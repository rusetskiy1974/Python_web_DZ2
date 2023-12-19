from rich.console import Console as RichConsole

console = RichConsole()


class Console:
    @staticmethod
    def print_error(text: str):
        console.print(':cross_mark: ', text, style='red')

    @staticmethod
    def print_success(text: str):
        console.print(':party_popper:', text, style='chartreuse1')

    @staticmethod
    def print_tip(text: str):
        console.print(':sparkles:', text, style='wheat1')

    @staticmethod
    def input(text: str):
        return console.input(prompt=f':clipboard: [sky_blue3]{text}[/]', markup=True, emoji=True, password=False, stream=None)

    @staticmethod
    def print(text: str, justify='left'):
        console.print(text, justify=justify)

