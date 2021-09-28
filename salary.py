import main2

@main2.decorator
def calculate_salary():
    return 'Функция calculate_salary запущена'


calculate_salary()