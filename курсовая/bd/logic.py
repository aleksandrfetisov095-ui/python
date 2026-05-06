from prettytable import PrettyTable


def show_table(data, title="Автомобили"):
    """Выводит данные в виде таблицы PrettyTable."""
    if not data:
        print("База данных пуста.")
        return

    table = PrettyTable()
    table.title = title
    table.field_names = ["Название", "Марка", "Мощность", "Гарантия (км)", "Гарантия (лет)", "Клиренс", "Цена",
                         "Уд. ст."]
    table.align["Название"] = "l"
    table.align["Марка"] = "l"
    table.align["Уд. ст."] = "r"

    for name, vals in data.items():

        power, guar_km, price = vals[1], vals[2], vals[5]
        ud_cost = price / guar_km if guar_km != 0 else 0

        table.add_row([
            name,
            vals[0],
            int(power),
            int(guar_km),
            int(vals[3]),
            int(vals[4]),
            int(price),
            f"{ud_cost:.2f}"
        ])

    print(table)


def add_records_interactive(cars):
    """Добавление новых записей через консоль."""
    try:
        n = int(input("Сколько записей добавить? "))
    except ValueError:
        print("Некорректное число.")
        return

    for _ in range(n):
        print("\n--- Новая запись ---")
        name = input("Название авто: ").strip()
        if not name:
            continue

        if name in cars:
            print(f"Авто '{name}' уже есть. Данные будут обновлены.")

        maker = input("Марка авто: ").strip()

        try:
            power = float(input("Мощность (л.с.): "))
            guar_km = float(input("Гарантия по пробегу (тыс. км): "))
            guar_years = float(input("Гарантия (лет): "))
            clearance = float(input("Клиренс (мм): "))
            price = float(input("Стоимость (тыс. руб.): "))

            cars[name] = [maker, power, guar_km, guar_years, clearance, price]
            print("Запись сохранена в память.")
        except ValueError:
            print("Ошибка ввода чисел. Запись пропущена.")


def delete_record_interactive(cars):
    """Удаление записи по названию с подтверждением."""
    name = input("Введите название авто для удаления: ").strip()

    if name not in cars:
        print("Нет такой записи.")
        return False

    # Запрос подтверждения
    confirm = input(f"Вы действительно хотите удалить '{name}'? Это действие нельзя отменить. (д/н): ").lower()

    if confirm == 'д' or confirm == 'y':
        del cars[name]
        print("Запись удалена из памяти.")
        return True
    else:
        print("Удаление отменено.")
        return False


def search_menu(cars):
    """
    Расширенный поиск: позволяет выбрать критерий поиска.
    Возвращает словарь найденных автомобилей или пустой словарь.
    """
    if not cars:
        print("База данных пуста.")
        return {}

    print("\n--- Меню поиска ---")
    print("1. По названию автомобиля")
    print("2. По марке производителя")
    print("3. По цене (диапазон)")
    print("4. По мощности (диапазон)")
    print("5. Выход из поиска")

    choice = input("Выберите тип поиска (1-5): ").strip()

    found_cars = {}

    if choice == '1':
        query = input("Введите часть названия: ").lower()
        found_cars = {k: v for k, v in cars.items() if query in k.lower()}

    elif choice == '2':
        query = input("Введите часть названия марки: ").lower()
        found_cars = {k: v for k, v in cars.items() if query in v[0].lower()}

    elif choice == '3':
        try:
            min_price = float(input("Минимальная цена (тыс. руб.): "))
            max_price = float(input("Максимальная цена (тыс. руб.): "))
            # Price is at index 5
            found_cars = {k: v for k, v in cars.items() if min_price <= v[5] <= max_price}
        except ValueError:
            print("Ошибка ввода чисел.")

    elif choice == '4':
        try:
            min_power = float(input("Минимальная мощность (л.с.): "))
            max_power = float(input("Максимальная мощность (л.с.): "))
            # Power is at index 1
            found_cars = {k: v for k, v in cars.items() if min_power <= v[1] <= max_power}
        except ValueError:
            print("Ошибка ввода чисел.")

    elif choice == '5':
        return {}

    else:
        print("Неверный выбор.")
        return {}

    if found_cars:
        print(f"\nНайдено записей: {len(found_cars)}")
        show_table(found_cars, title="Результаты поиска")
    else:
        print("Ничего не найдено по заданным критериям.")

    return found_cars


def calc_ud_costs(cars):
    """Расчет и вывод удельной стоимости для всех авто."""
    if not cars:
        print("База пуста.")
        return

    sorted_cars = sorted(cars.items(), key=lambda x: x[1][5] / x[1][2] if x[1][2] != 0 else float('inf'))

    table = PrettyTable()
    table.title = "Удельная стоимость (Цена / Гарантия по пробегу)"
    table.field_names = ["Название", "Марка", "Цена", "Гарантия (км)", "Уд. ст."]
    table.align["Уд. ст."] = "r"

    for name, vals in sorted_cars:
        price, guar_km = vals[5], vals[2]
        ud = price / guar_km if guar_km != 0 else 0
        table.add_row([name, vals[0], int(price), int(guar_km), f"{ud:.2f}"])

    print(table)


def sort_by_ud_for_manufacturers(cars):
    """Сортировка по удельной стоимости для двух выбранных производителей."""
    if not cars:
        print("База пуста.")
        return

    makers = sorted(set(v[0] for v in cars.values()))
    if not makers:
        return

    print("Доступные производители:")
    for i, m in enumerate(makers, 1):
        print(f"{i}. {m}")

    try:
        idx1 = int(input("\nВыберите номер первого производителя: ")) - 1
        idx2 = int(input("Выберите номер второго производителя: ")) - 1

        if not (0 <= idx1 < len(makers)) or not (0 <= idx2 < len(makers)):
            print("Неверный выбор номера.")
            return

        m1, m2 = makers[idx1], makers[idx2]

    except (ValueError, IndexError):
        print("Ошибка ввода.")
        return

    if m1 == m2:
        print("Выберите разных производителей.")
        return

    filtered = {k: v for k, v in cars.items() if v[0] == m1 or v[0] == m2}

    if not filtered:
        print("Нет авто от указанных производителей.")
        return

    sorted_items = sorted(filtered.items(), key=lambda x: x[1][5] / x[1][2] if x[1][2] != 0 else float('inf'))
    show_table(dict(sorted_items), title=f"Сравнение: {m1} и {m2}")
