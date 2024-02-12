import os
from typing import List

def display_menu() -> str:
    """
    Выводит меню и возвращает выбранный пользователем пункт.
    """
    print("Телефонный справочник")
    print("1. Вывести все записи")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("5. Выйти")

    choice: str = input("Выберите действие: ")
    return choice

def read_entries() -> List[List[str]]:
    """
    Читает записи из файла и возвращает список списков строк.
    """
    entries: List[List[str]] = []
    with open("phonebook.txt", "r") as file:
        for line in file:
            entry = line.strip().split(',')
            entries.append(entry)
    return entries

def write_entries(entries: List[List[str]]) -> None:
    """
    Записывает записи в файл.
    """
    with open("phonebook.txt", "w") as file:
        for entry in entries:
            file.write(','.join(entry) + '\n')

def display_entries(entries: List[List[str]]) -> None:
    """
    Выводит записи на экран.
    """
    for entry in entries:
        print(', '.join(entry))

def add_entry() -> List[str]:
    """
    Запрашивает у пользователя новую запись и возвращает ее в виде списка строк.
    """
    new_entry: str = input("Введите данные в формате: Фамилия, Имя, Отчество, Название организации, Рабочий телефон, Личный телефон: ")
    return new_entry.split(',')

def edit_entry(entries: List[List[str]]) -> None:
    """
    Редактирует выбранную запись.
    """
    display_entries(entries)
    index: int = int(input("Введите индекс записи для редактирования: "))
    if index < len(entries):
        new_data: str = input("Введите новые данные в формате: Фамилия, Имя, Отчество, Название организации, Рабочий телефон, Личный телефон: ")
        entries[index] = new_data.split(',')
    else:
        print("Неверный индекс записи")

def search_entries(entries: List[List[str]]) -> None:
    """
    Ищет записи по введенной пользователем строке и выводит результаты на экран.
    """
    search_query: str = input("Введите строку для поиска: ")
    results: List[List[str]] = [entry for entry in entries if any(search_query.lower() in field.lower() for field in entry)]
    display_entries(results)

def main() -> None:
    """
    Основная функция программы.
    """
    # Если файл не существует, создаем его
    if not os.path.exists("phonebook.txt"):
        open("phonebook.txt", "w").close()

    while True:
        choice: str = display_menu()

        if choice == '1':
            entries: List[List[str]] = read_entries()
            display_entries(entries)
        elif choice == '2':
            new_entry: List[str] = add_entry()
            entries: List[List[str]] = read_entries()
            entries.append(new_entry)
            write_entries(entries)
        elif choice == '3':
            entries: List[List[str]] = read_entries()
            edit_entry(entries)
            write_entries(entries)
        elif choice == '4':
            entries: List[List[str]] = read_entries()
            search_entries(entries)
        elif choice == '5':
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()