#13.1
import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]*>', '', html)
    lines = cleaned_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    lines_with_spaces = [line for line in non_empty_lines if ' ' in line]
    final_text = '\n'.join(lines_with_spaces)

    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(final_text)
#13.2
class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, ціна: {self.price} грн, {self.description}, {self.dimensions}"


class User:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}, тел.: {self.phone}"


class Order:
    def __init__(self, user):
        self.user = user
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def __str__(self):
        result = f"Замовлення для: {self.user}\nТовари:\n"
        for item, quantity in self.items.items():
            result += f"  {item} x {quantity} = {item.price * quantity} грн\n"
        result += f"Загальна вартість: {self.total_price()} грн"
        return result


# Тестування
if __name__ == "__main__":
    apple = Item("Яблуко", 15, "свіже", "10x10x10 см")
    banana = Item("Банан", 25, "стиглий", "15x5x5 см")
    milk = Item("Молоко", 30, "пастеризоване", "20x10x10 см")

    user = User("Петренко", "Іван", "Олегович", "0981234567")

    order = Order(user)
    order.add_item(apple, 3)
    order.add_item(banana, 2)
    order.add_item(milk, 1)

    print(order)