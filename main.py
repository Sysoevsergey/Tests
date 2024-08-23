def check_age(age: int):

    if age >= 18: # Введите условие для проверки возраста
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'
    return result


def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
        result = ('Добро пожаловать')
    else:
        result = ('Доступ ограничен')

    return result


def get_cost(weight: int):
    if weight <= 10 and weight > 0:
        return('Стоимость доставки: 200 руб.')
    elif weight >= 11:
        return('Стоимость доставки: 500 руб.')
    else:
        return('Ошибка ввода данных')


def new_func(*args, **kwargs):
    return('Функция пока не реализована')
