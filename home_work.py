#Ex 7.1
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"
#Ex 7.2
def correct_sentence(text):
    text = text[0].upper() + text[1:] if text else text
    if not text.endswith('.'):
        text += '.'
    return text
#Ex 7.3
def second_index(text, some_str):
    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + 1)
    return second if second != -1 else None
#Ex 7.4
def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    return multiples_of_3 & multiples_of_5
