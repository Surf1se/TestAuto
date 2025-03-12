def age_message(birthday):
    age = 2025 - birthday
    print(f'Ваш возраст: {age}')
    if age < 18 :
        print("Вы еще молоды, учеба — ваш путь!")
    elif age >= 18 and age <= 65 :
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")


birthday = int(input('Введите год вашего рождения: '))

age_message(birthday)
