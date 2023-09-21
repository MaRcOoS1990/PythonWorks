from data_create import *


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
