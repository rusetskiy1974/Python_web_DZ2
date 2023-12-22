from user_assistant.console.console import Console
import keyboard
import pyperclip

def write(text):
    pyperclip.copy(text)  
    pyperclip.paste()


def input_value(value: str, class_field: classmethod, is_edit=False, old_value = None, placeholder=None):
    while True:
        if old_value:
            print(f'Change old {value} :', end='')
            write(old_value)
            keyboard.press('ctrl+v') 
            keyboard.release('ctrl+v')
            result = input()
            pyperclip.copy('')
        else:    
            result = Console.input(f'Enter {value}: ', placeholder=placeholder).strip()
        if result == '' and is_edit:
            return result
        try:
            result = class_field(result)
            return result
        except Exception as error:
            Console.print_error(error)
            continue
