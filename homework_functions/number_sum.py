n = int(input('Введите число: '))

def summa():
    print('Числа: ', end="")
    for k in range(1,n + 1):
        print(f'{k} ',end = "")
        summa = sum( int(i) for i in range(1,n + 1))
    print(f'\nСумма чисел: {summa}')


summa()
