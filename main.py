from user_assistant.main import main
import re


str = str(Exception('The date is incorrect. The format should be [12.10.1994]'))

res = re.findall(r'\[.*\]', str)[0]
updated_format = re.sub("[\[\]]","", res)
new_str = str.replace(res, f'[bold]{updated_format}[/]')

if __name__ == '__main__':
    main()