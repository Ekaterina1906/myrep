try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print(number1 / number2)
except (ValueError, ZeroDivisionError):
    print("Это не число или деление на ноль")

print("Программа завершена")



filename = input("Введите путь к файлу, который хотите прочитать: ")
myfile = open(filename)
line = myfile.readline()
num = 0
while line != "":
    print(line)

    num = num + 1
    line = myfile.readline()

myfile.close()