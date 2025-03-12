"""

Добавленеи бага
присвоение ему приоритета
добавление его в  массив
сортировка по приоритету (high / low)

"""
bugContainerHigh = []
bugContainerLow = []
i = 0

bugReportCount = int(input("Сколько багов Вы хоитите добавить? "))

while i < bugReportCount:
    bagName = input("Напишите название бага : ")
    priorityBug = input("Какой приоритет у бага? (low | high) ")
    bugReportName = bagName + " - " + priorityBug

    if priorityBug == "high":
        bugContainerHigh.append(bugReportName)
        i += 1
    elif priorityBug == "low":
        bugContainerLow.append(bugReportName)
        i += 1
    else:
        print("Произошла ошибка при добавлении бага, проверьте заполнения полей.")

print()
print("--------------------")
print("Баги с высоким приоритетом :")
print(bugContainerHigh)
print("--------------------")
print("Баги с низким приоритетом :")
print(bugContainerLow)
print("--------------------")
