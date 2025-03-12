# Функция вывода приветствия
def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать в мир Python!")


# Функцияи для вывода суммы чисел
def calculate_sum(a, b):
    sum = a + b
    print(f'Сумма чисел: {sum}')


name = input('Введите ваше имя: ')
greet_user(name)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

calculate_sum(a,b)
