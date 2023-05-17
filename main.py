class Todo:
    menu = {'1' :'Добавить дело', '2' :'Список всех дел', '3' :'Найти дело', '4' :'Выполнить дело', '5' :'Повторить дело', '6' :'Выйти'}

    def __init__(self):
        self.todo_items = []
        
    def add_todo(self, items):
        self.todo_items.append(items)
        print('Задача успешно добавлена')

    def list(self):
        for name in TodoItem:
            print(name)


    def find(self):
        pass

    def run(self):
        while True:
            print('Меню:')
            for key, val in Todo.menu.items():
                print(key + '.' + val, end='\n')

            command = input('Введите номер команды: ')

            if command == '1':
                pass
            elif command == '2':
                pass
            elif command == '3':
                pass
            elif command == '4':
                pass
            elif command == '5':
                pass
            elif command == '6':
                print('Программа завершена')
            break


class TodoItem:
    counter_do = 0

    def __init__(self, new_do):
        self.is_done = False
        self.name = new_do

        TodoItem.counter_do += 1 
        self.counter = TodoItem.counter_do

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False


#if name == 'main':
todo = Todo()
todo.run()