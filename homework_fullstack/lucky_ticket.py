mainNumber = input("Введите номер билета: ")
mainNumber = str(mainNumber)

x = 0
y = 0
i = 0
k = 3


while i < 3:
    x += int(mainNumber[i])
    i += 1
while k < 6:
    y += int(mainNumber[k])
    k += 1

#print("x = ",x)
#print("y = ",y)

if x == y:
    print("Результат: билет счастливый.")
else:
    print("Результат: билет несчастливый.")

