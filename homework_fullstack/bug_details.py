bugDetails = {
    "id"     : None,
    "name"   : None,
    "status" : None
}

while True:
    post = input("Что хотите изменить в баге? id, name, status , нет?")
    post = post.lower()

    if post == "id":
        new = input("ID = ")
        bugDetails["id"] = new

        endProgram = input("Хотите еще что-то изменить? да или нет ")
        endProgram = endProgram.lower()
        if endProgram == "нет":
            break

    elif post == "name":
        new = input("name = ")
        bugDetails["name"] = new

        endProgram = input("Хотите еще что-то изменить? да или нет ")
        endProgram = endProgram.lower()
        if endProgram == "нет":
            break

    elif post == "status":
        new = input("status = ")
        bugDetails["status"] = new

        endProgram = input("Хотите еще что-то изменить? да или нет ")
        endProgram = endProgram.lower()
        if endProgram == "нет":
            break

    elif post == "нет":
        break

    else:
        print("Не понял, Ваш ответ, пожалуйста проверьте его.")

print(bugDetails)
