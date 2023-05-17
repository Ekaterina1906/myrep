class lion:
    

    def __init__(self, age, weight, dlina, shirina, color, dlina_chvosta):
        self.__age = age
        self.__weight = weight
        self.__dlina = dlina
        self.__shirina =shirina
        self.__color = color
        self.__dlina_chvosta = dlina_chvosta

    def  say(self):
        print("Ррррр")

    def getAge(self):
        print(self.__age)

    def setAge(self, new_age):
        if 0 < new_age >= 26:
            print("Возраст задан некорректно!")
        else:
            self.__age = new_age

    def getColor(self):
        print(self.__color)

    def setColor(self, new_color):
        self.__color = new_color


class cat(lion):
    __default_name = "Murzik"
        
    def __init__(self , name, color, age, weight, dlina, shirina, dlina_chvosta):
        super().__init__(age, weight, dlina, shirina, color, dlina_chvosta)
        if name:
            self.__name = name
        else:
            self.__name = cat.__default_name

    @staticmethod
    def print_name():
        print(cat.__default_name)

    
    def getName(self):
        print(self.__name)

    def setName(self, new_name):
        if len(new_name) <= 15:
            self.__name = new_name
        else:
            print("Имя не должно превышать 15 символов")

    
    def say_cat(self):
        print("Мяу")


def check_type(animal):
    if isinstance(animal, cat):
        animal.say_cat()
    elif isinstance(animal, lion):
        animal.say()


lion1 = lion(10, 35, 50, 20, "white", 25)
cat1 = cat("Pushok","black", 5, 4, 25, 10, 12)
check_type(lion1)
check_type(cat1)
cat1.getName()