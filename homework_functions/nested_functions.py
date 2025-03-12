def calculator():

    # Функция для вычисления суммы
    def summa(number_1, number_2):
        res = number_1 + number_2
        print(f'{res}')


    # Функция для вычисления разности
    def rasnost(number_1, number_2):
        res = number_1 - number_2
        print(f'{res}')


    # Функция для вычисления произведения
    def umnojenie(number_1, number_2):
        res = number_1 * number_2
        print(f'{res}')


    # Функция для вычисления частного
    def delenie(number_1, number_2):
        if number_2 == 0:
            print('Ошибка! Деление на ноль!')
        else:
            res = number_1 / number_2
            print(f'{res}')


    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    c = input('Выберите операцию (+, -, *, /): ')

    print('Результат: ', end='')

    if c == '+':
        summa(number_1, number_2)
    elif c == '-':
        rasnost(number_1, number_2)
    elif c == '*':
        umnojenie(number_1, number_2)
    elif c == '/':
        delenie(number_1, number_2)
    else:
        print('Ошибка! Выберите корректную операцию')


calculator()
