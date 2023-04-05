#km = float(input("Введите количество километров: "))
#a = 0.621371
#mili = km * a
#print(f'{km} километров - это {round(mili, 2)} миль')


#def km1():
#    a = float(input("Введите количество километров: "))
#    b = 0.621371
#    mili1 = a * b
#    return mili1
#print(km1())


#def c1():
#    c = float(input("Введите значение в градусах Цельсия: "))
#    f =(c * 1.8) + 32
#    return f
#print(c1())



#def average(n1,n2):
#    m = (n1 + n2) / 2
#    return m
#a = int(input("А = "))
#b = int(input("В = "))

#avrg = average(a,b)
#print(round(avrg,2))


#print(os.getcwd())

#if not os.path.isdir("My new folder1"):
#    os.mkdir("My new folder1")
#print(os.listdir(os.getcwd()))


#myTextFile = open("Новый текстовый файл.txt","w")
#myTextFile.write("привет")
#myTextFile.close()


#if os.path.isfile('Новый текстовый документ.txt'):
#    print(myTextFile.readlihes())



#def read_last(lines, file):
#    if lines > 0:
#        with open(file) as text:
#            file_lines = text.readlines()[-lines:]
#        for line in file_lines:
#            print(line.strip())
#    else:
#        print("Количество строк может быть только целым положительным")

#   # print(os.getcwd())
#read_last(3, 'Новый текстовый файл.txt')



#import os

#print(os.getcwd())

#if not os.path.isdir('Куташова'):
#    os.mkdir('Куташова')

#os.chdir('Куташова')
#myFile = open('Катерина.txt','w')   
#myFile.write("В центре планетарной туманности Южный краб находятся пара звед; холодный, пульсирующий красный гигант и горячий белый карлик;") 
#myFile.close()

#myFile1 = open('Катерина.txt','r')
#text = myFile1.read()
#print(text)


def sum():
    b = int(input("Введите число: "))
    a = int(input("Введите число: "))
    print(a + b)

def sum():
    b = int(input("Введите число: "))

    a = int(input("Введите число: "))
    print(a * b)
print(1)
print()
