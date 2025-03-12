def check_triangle(storona_1, storona_2, storona_3):
# Проверка условия существования треугольника
    if storona_1 > storona_2 + storona_3 \
    or storona_2 > storona_1 + storona_3 \
    or storona_3 > storona_1 + storona_2:
        print('Ошибка: треугольник с такими сторонами не может существовать')
# Следующие 2 строчки по большому счету не нужны, но захотелось так сделать
    else:
        print('Результат: ', end='')
        if storona_1 == storona_2 == storona_3:
            print('Треугольник равносторонний')
        elif storona_1 == storona_2 or storona_2 == storona_3 or storona_1 == storona_3:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')

storona_1 = int(input('Введите длину первой стороны: '))
storona_2 = int(input('Введите длину второй стороны: '))
storona_3 = int(input('Введите длину третей стороны: '))

check_triangle(storona_1, storona_2, storona_3)
