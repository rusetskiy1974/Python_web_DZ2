def input_value(value: str, class_field: classmethod, is_edit = False):
    while True:
        result = input(f'Enter {value}: ')
        if result == '' and is_edit:
            return result
        try:
            result = class_field(result)
            return result
        except Exception as error:
            print(error)
            continue
