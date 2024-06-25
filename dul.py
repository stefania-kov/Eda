class Dish:
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = int(price)
        self.weight = int(weight)

    def __str__(self):
        return f"Dish: {self.name}, Категория: {self.category}, Стоимость: {self.price}, Вес: {self.weight}"


class Menu:
    def __init__(self, filename="ty.txt"):
        self.menu_dict = self.read_menu_from_file(filename)

    def __iter__(self):
        """Позволяет итерировать по блюдам в меню."""
        return iter(self.menu_dict.values())

    def read_menu_from_file(self, filename):
        """Считывает данные о блюдах из файла."""
        menu_dict = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(';')
                    if len(parts) == 4:
                        name, category, price, weight = parts
                        try:
                            price = int(price)
                            weight = int(weight)
                            menu_dict[name] = Dish(name, category, price, weight)
                        except ValueError:
                            print(f"Некорректная стоимость или вес для блюда: {name}")
                    else:
                        print(f"Некорректная строка: {line.strip()}")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        return menu_dict

"# Eda" 
