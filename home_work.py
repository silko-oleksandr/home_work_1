#10.1
def some_gen(begin, end, func):
    current = begin
    for _ in range(end):
        yield current
        current = func(current)
#10.2
def first_word(text):
    for i, char in enumerate(text):
        if char.isalpha() or char == "'":
            start = i
            break
    for i in range(start, len(text)):
        if not (text[i].isalpha() or text[i] == "'"):
            return text[start:i]
    return text[start:]
#10.3
def is_even(digit):
    """
    Перевірка чи є парним число
    """
    return digit % 2 == 0