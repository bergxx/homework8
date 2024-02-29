import os
import json

phone_book = []
phone_book_file = "telephonedirectory.json" 

def show_menu():
    print("\nВыберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента\n",
          "3. Добавить абонента в справочник\n",
          "4. Изменить абонента\n",
          "5. Удалить абонента\n",
          "6. Сохранить справочник в текстовом формате\n",
          "7. Копировать строку из файла\n",
          "8. Закончить работу")
    choice = int(input())
    return choice

def show_search_menu():
    print("\nВыберите вариант поиска:\n",
          "1. Поиск по имени\n",
          "2. Поиск по фамилии\n",
          "3. Поиск по телефону\n",
          "4. Поиск по комментарию\n",
          "5. Отменить\n")
    search_mod = int(input())
    return search_mod

def load_phone_book(phone_book_file):
    with open(phone_book_file, "r", encoding="utf-8") as f:
        return json.load(f)

def sort_data_by_name(data):
    sorted_data = sorted(data, key=lambda x: (x["surname"], x["name"]))
    return sorted_data

def save_phone_book(phone_book, phone_book_file = "telephonedirectory.json"):
    phone_book = sort_data_by_name(phone_book)
    with open(phone_book_file, "w", encoding="utf-8") as f:
        json.dump(phone_book, f, indent=4, ensure_ascii=False)
    print("="*len("Данные записной книги обновлены"))
    print("Данные записной книги обновлены")
    print("="*len("Данные записной книги обновлены"))

def show_contacts(contacts):
    if contacts == None:
        os.system('cls||clear')
        print("По данному запросу нет контактов для отображения")
        return
    max_name_len = max(len(contact["name"]) for contact in contacts)
    max_surname_len = max(len(contact["surname"]) for contact in contacts)
    max_phone_len = max(len(contact["phone"]) for contact in contacts)
    max_description_len = max(len(contact["description"]) for contact in contacts)
    print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("Фамилия", max_surname_len, "Имя", max_name_len, "Телефон", max_phone_len, "Описание", max_description_len))
    print("-" * (max_surname_len + max_name_len + max_phone_len + max_description_len + 13))
    # Вывод контактов
    for contact in contacts:
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(
            contact["surname"], max_surname_len, contact["name"], max_name_len, contact["phone"], max_phone_len, contact["description"], max_description_len
        ))

def find_contact(contacts):
    if contacts == None: 
        print("Вы ввели некорректные данные, попробуйте еще раз")
    search_mod = show_search_menu() 
    search_str = None
    data = []
    while True:
        if search_mod == 1:
            search_mod = "name"
            search_str = input("Введите имя для поиска: ")
            break
        elif search_mod==2:
            search_mod = "surname"
            search_str = input("Введите фамилию для поиска: ")
            break
        elif search_mod==3:
            search_mod = "phone"
            search_str = input("Введите телефон для поиска: ")
            break
        elif search_mod==4:
            search_mod = "description"
            search_str = input("Введите описание для поиска: ")
            break
        elif search_mod==5:
            return None
        search_mod=show_search_menu()
    for contact in contacts: 
        if search_str.lower() in contact[search_mod].lower():
            data.append(contact)
    if len(data) > 0: 
        return data
    return None

def add_contact(contacts):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    new_contact = {"surname": surname, "name": name, "phone": phone, "description": description}
    contacts.append(new_contact)
    return contacts

def remove_contact(contacts, contact_to_del):
    remove_index = None 
    if contact_to_del == None or len(contact_to_del) == 0:
        print("Такого контакта не найдено")
        return
    elif len(contact_to_del) == 1:
        remove_index = 0
    else:
        show_contacts(contact_to_del)
        print("Введите порядковый номер контакта для удаления")
        remove_index = int(input()) - 1
    contacts.remove(contact_to_del[remove_index])
    return contacts

def edit_contact(contacts):
    contact = find_contact(contacts)
    choice = None
    if contact is None:
        print("Контакт не найден.")
        return
    elif len(contact) > 1:
        show_contacts(contact)
        print("Введите номер контакта для изменения")
        choice = int(input()) - 1
    if choice != None and choice + 1 <= len(contact):
        contact = contact[choice]
    else:
        contact = contact[0]

    print("Введите данные для обновления или нажмите Enter чтобы оставить как было:")
    name = input("Имя: ") or contact["name"]
    surname = input("Фамилия: ") or contact["surname"]
    phone = input("Номер телефона: ") or contact["phone"]
    description = input("Описание: ") or contact["description"]
    
    contact["surname"] = surname
    contact["name"] = name
    contact["phone"] = phone
    contact["description"] = description
    return contacts

def save_contacts_to_txt(contacts, file_name = "telephone_directory.txt"):
    if contacts == None:
        os.system('cls||clear')
        print("По данному запросу нет контактов для отображения")
        return
    max_name_len = max(len(contact["name"]) for contact in contacts)
    max_surname_len = max(len(contact["surname"]) for contact in contacts)
    max_phone_len = max(len(contact["phone"]) for contact in contacts)
    max_description_len = max(len(contact["description"]) for contact in contacts)
    with open(file_name, "w") as f:
        f.write("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |\n".format("Фамилия", max_surname_len, "Имя", max_name_len, "Телефон", max_phone_len, "Описание", max_description_len))
        f.write("-" * (max_surname_len + max_name_len + max_phone_len + max_description_len + 13) + "\n")
        for contact in contacts:
            f.write("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |\n".format(
                contact["surname"], max_surname_len, contact["name"], max_name_len, contact["phone"], max_phone_len, contact["description"], max_description_len
            ))

def copy_contact_from_file(source_file):
    try:
        with open(source_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        index = int(input("Введите номер строки для копирования: ")) - 1
        if 0 <= index < len(data):
            return data[index]
        else:
            print("Некорректный номер строки.")
            return None
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    except json.JSONDecodeError:
        print("Некорректный формат файла JSON.")
        return None

def import_contacts_from_txt(file_name):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            contacts = []
            for line in lines[2:]:  # Skip header line
                parts = line.strip().split(" | ")
                surname, name, phone = parts[1], parts[3], parts[5]
                contacts.append({"surname": surname, "name": name, "phone": phone})
            return contacts
    except FileNotFoundError:
        print("Файл не найден.")
        return []

def export_contacts_to_txt(phone_book, file_name="exported_contacts.txt"):
    with open(file_name, "w") as f:
        for contact in phone_book:
            f.write(f'{contact["surname"]} | {contact["name"]} | {contact["phone"]}\n')

def work_with_phonebook(phone_book_file):
    choice = show_menu()
    while choice != 8:
        phone_book = load_phone_book(phone_book_file)
        if choice == 1:
            os.system('cls||clear')
            show_contacts(phone_book)
        elif choice == 2:
            os.system('cls||clear')
            show_contacts(find_contact(phone_book))
        elif choice == 3:
            os.system('cls||clear')
            add_contact(phone_book)
            save_phone_book(phone_book, phone_book_file)
        elif choice == 4:
            os.system('cls||clear')
            edit_contact(phone_book)
            save_phone_book(phone_book, phone_book_file)
        elif choice == 5:
            os.system('cls||clear')
            remove_contact(phone_book, find_contact(phone_book))
            save_phone_book(phone_book, phone_book_file)
        elif choice == 6:
            os.system('cls||clear')
            save_contacts_to_txt(phone_book)
        elif choice == 7:
            os.system('cls||clear')
            source_file = input("Введите имя файла, из которого нужно скопировать строку: ")
            contact_to_copy = copy_contact_from_file(source_file)
            if contact_to_copy:
                phone_book.append(contact_to_copy)
                save_phone_book(phone_book, phone_book_file)
        choice = show_menu()
    os.system('cls||clear')
    print("Вы закончили работу с записной книгой")

work_with_phonebook(phone_book_file)