from datetime import datetime
import os

folder_path = os.getcwd()
with open('output.txt', 'w') as file:
    file.write('')


def parametrized_decorator(parameter):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            current_datetime = datetime.strftime(datetime.now(), "%c")
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            parameter = os.getcwd()
            with open('output.txt', 'a') as file:
                file.write(f'{current_datetime}. Название функции: {func_name}. Аргументы: {[*args]}. Возвращаемое '
                           f'значение: {old_function(*args, **kwargs)}. Путь к логам: {parameter} \n')
            return result
        return new_function
    return decorator


@parametrized_decorator(folder_path)
def minus(a, b):
    return a - b

minus(4, 6)
minus(5, 8)

@parametrized_decorator(folder_path)
def person(name, surname):
    data = f'His name is {name}. His surname is {surname}.'
    return data

person('John', 'Bull')
person('Walter', 'Scott')
