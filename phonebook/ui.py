from logger import *


def interface():
    cmd = 0
    while cmd != '4':
        print('Вариант действий:\n'
              '1. Добавить контакт\n'
              '2. Вывести все контакты\n'
              '3. Поиск контакта\n'
              '4. Выход')
        cmd = input('Введите действие:')
        while cmd not in ('1', '2', '3', '4'):
            print('Некоректный ввод')
            cmd = input('Введите действие:')
        match cmd:
            case'1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                print('Всего доброго!')
