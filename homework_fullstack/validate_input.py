# прроверка корректности записи строк или числа\

while True:
    age = input("age : ")
    if not age.isdigit():
        print ("нужно только цифры")
    else:
        if 0 <= int(age) <= 120:
            print("отлично")
            break
        else:
            print("Некорректный возраст")

while True:
    name = input("name :")
    if name.isalpha():
        print("отлично")
        break
    else:
        print("нужно только буквы")

print("ahyenno, teper zakon4ili")
