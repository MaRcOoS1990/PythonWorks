from phone_book_data_create import *


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


def deleted_contact():
    print('Выберите вариант поиска:\n'
          '1. Фамилия \n'
          '2. Имя \n'
          '3. Отчество \n'
          '4. Телефон \n'
          '5. Адрес ')
    index = int(input('Введите вариант: '))-1
    searched = input('Введиде данные для удаления:').title()
    print()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

    for item in data:

        if searched in item:
            data.remove(item)

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def change_contact():
    print('Выберите вариант изменения:\n'
          '1. Фамилия \n'
          '2. Имя \n'
          '3. Отчество \n'
          '4. Телефон \n'
          '5. Адрес ')
    index = int(input('Введите вариант: '))-1
    searched = input('Ввеберите данные которые изменяем:').title()
    item_change = input('Введите данные на которые изменяем:').title()
    print()
    new_data = []
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

        for item in data:
            new_item = item.replace('\n', ' ').split()
            if new_item[index] == searched:
                new_item[index] = item_change
                new_data.append(
                    f'{new_item[0]} {new_item[1]} {new_item[2]}\n{new_item[3]}\n{new_item[4]}\n')
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))
