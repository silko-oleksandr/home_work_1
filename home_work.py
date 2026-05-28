#13.1
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]*>', '', html)
    lines = cleaned_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    lines_with_spaces = [line for line in non_empty_lines if ' ' in line]
    final_text = '\n'.join(lines_with_spaces)

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(final_text)
#13.2
from typing import Dict

class Item:
    def __init__(self, name: str, price: float, description: str, dimensions: str):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f"{self.name}, ціна: {self.price} грн, {self.description}, {self.dimensions}"


class User:
    def __init__(self, surname: str, name: str, patronymic: str, phone: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}, тел.: {self.phone}"


class Order:
    def __init__(self, user: User):
        self.user = user
        self.items: Dict[Item, int] = {}

    def add_item(self, item: Item, quantity: int = 1) -> None:
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def total_price(self) -> float:
        total = 0.0
        for item, quantity in self.items.items():
            total += item.price * quantity
        return total

    def __str__(self) -> str:
        result = f"Замовлення для: {self.user}\nТовари:\n"
        for item, quantity in self.items.items():
            result += f"  {item} x {quantity} = {item.price * quantity} грн\n"
        result += f"Загальна вартість: {self.total_price()} грн"
        return result


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