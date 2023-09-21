# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def enter_family_name():
    return input('Введите фамилию абонента:').title()


def enter_first_name():
    return input('Введите имя абонента:').title()


def enter_second_name():
    return input('Введите отчество абонента:').title()


def enter_phone_number():
    return input('Введите телефонный номер абонента:').title()


def enter_address_number():
    return input('Введите адрес абонента:').title()


def enter_data():
    family = enter_family_name()
    name = enter_first_name()
    surname = enter_second_name()
    numbers = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{family} {name} {surname}\n{numbers}\n{address}\n\n')


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('Выберите вариант поска:\n'
          '1. Фамилия \n'
          '2. Имя \n'
          '3. Отчество \n'
          '4. Телефон \n'
          '5. Адрес ')
    index = int(input('Введите вариант: '))-1
    searched = input('Введиде данные для поиска:').title()
    print()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item)
                print()
        # file.seek(0)
        # print(file.readlines())


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


interface()
1
