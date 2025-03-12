name = "Andrey"
toolForWork = "Postman"
professia = "QA"

print(f"Ваш профиль выглядит так: , Имя : {name}, Инстумент для работы : {toolForWork}, Проффесия : {professia}")

mb = input("Хотите что-то зменить? Да или Нет ")
mb = mb.lower()

if mb != "да":
    print("Хорошо, данные остаются прежними. Хорошего дня!")
else:
    while True:
        what = input("Что вы хотите изменить? Имя, Инструмент, Проффесию? ")
        what = what.lower()

        print("------------------")

        if what == "имя":
            name = input("Измените имя. ")
            endProgram = input("Хотите еще что-то изменить? ")
            endProgram = endProgram.lower()
            if endProgram == "нет":
                break
            print("------------------")


        elif what == "инструмент":
            toolForWork = input("Измените инструмент ")
            endProgram = input("Хотите еще что-то изменить? ")
            endProgram = endProgram.lower()
            if endProgram == "нет":
                break
            print("------------------")


        elif what == "проффесию":
            toolForWork = input("Измените проффесию ")
            endProgram = input("Хотите еще что-то изменить? ")
            endProgram = endProgram.lower()
            if endProgram == "нет":
                break
            print("------------------")


        else:
            print("Проверьте правильность заполнения поля, я не понял, что Вы хотите изменить")
            print("------------------")


    print(f"Отлично, мы изменили данные, теперь они выглядят так :  Имя : {name}, Инстумент для работы : {toolForWork}, Проффесия : {professia} ")