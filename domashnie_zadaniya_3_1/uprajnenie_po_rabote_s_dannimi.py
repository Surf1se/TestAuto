# Функция для указания имени и почты
def contact():
    __operator = {
        "name" : "wqe",
        "mail" : "qwe@bk.ru"
    }
    return __operator


# Переменная с ответом от сервера
responce = {
    "state": 0,
    "data": []
}


# Main Функция
def responce_data():
    #Условие для провекрки, что в ответе есть заказы(Задание 1)
    responce_data_yes = bool(responce["data"])
    if responce_data_yes == True:
        if completion_time_orders() > 6:
            print("Время первого и второго заказов превышает 6 часов")
            order3()
            # Вывод отчета
            for i in report:
                print(report[i])
        else:
            order3()
            print('Все тесты пройдены успешно ')
            # Вывод отчета
            for i in report:
                print(report[i])

    else:
        print('Заказы не найдены в ответе от сервера.')


# Функция вычисления времени выполнения первого и второго заказов (задание 2)
def completion_time_orders():
    #Время выполнения первого заказа
    completion_time_order1 = int(responce["data"][0]["count"] * responce["data"][0]["delay"])
    #Время выполнения второго заказа
    completion_time_order2 = int(responce["data"][1]["count"] * responce["data"][1]["delay"])
    #Время выполнение первого и второго заказов
    completion_time_order1_and_order2 = completion_time_order1 + completion_time_order2
    return completion_time_order1_and_order2


# Функция для проверки, 3го заказа (задание 3)
def order3():
    #Кл-во услуг
    count_services = responce["data"][2]["count"]
    #Кл-во выполненых услуг
    completed_services = responce["data"][2]["completed"]
    #Кл-во услуг ожидающих возврата
    wait_refund_services = responce["data"][2]["wait_refund"]
    #Кл-во возвращенных услуг
    refunded_services = responce["data"][2]["wait_refund"]
    #Кл-во обработанных услуг
    processed_services = int(completed_services + wait_refund_services + refunded_services)

    # Проверка что для третьего заказа все услуги обработаны И выполнено не меньше половины
    if count_services == processed_services and \
            completed_services >=  (count_services / 2 )\
                or refunded_services <= completed_services \
                    and wait_refund_services <= refunded_services:
        print(end='')
    else:
        print("Не все услуги 3го заказа обработаны")


responce_data()


# Работа с формированием и выводом отчета
id_new = "326b23a1-e6ab-4b4a-84a1-a3ecb33afc97"

# Шаблон отчета для вывода
report = {
    "id" : [],
    "countWorkTask" : {
        "completed" : 0,
        "wait_refund" : 0,
        "refunded" : 0
    },
    "operator" : contact()
}

# Собираем отчет
k = 0
for i in responce["data"]:

    # Вытаскиеваем ID и каледм их в репорт
    id_inOrder = responce["data"][k]["_id"]
    report["id"].append(id_inOrder)

    # Вытаскиеваем обработаенные таски и кладем их в репорт
    completed_inOrder = responce["data"][k]["completed"]
    report["countWorkTask"]["completed"] += completed_inOrder

    wait_refund = responce["data"][k]["wait_refund"]
    report["countWorkTask"]["wait_refund"] += wait_refund

    refunded = responce["data"][k]["refunded"]
    report["countWorkTask"]["refunded"] += refunded

    k += 1

report["id"].append(id_new)
