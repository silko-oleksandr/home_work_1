#Ex 6.1
import string

user_input = input().strip()
first, second = user_input.split('-')
alphabet = string.ascii_letters
index1 = alphabet.index(first)
index2 = alphabet.index(second)
start = min(index1, index2)
end = max(index1, index2) + 1
print(alphabet[start:end])

#Ex 6.2
seconds = int(input().strip())

days = seconds // 86400
remainder = seconds % 86400
hours = remainder // 3600
remainder %= 3600
minutes = remainder // 60
secs = remainder % 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and days % 100 not in (12, 13, 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {hours:02d}:{minutes:02d}:{secs:02d}")
#Ex 6.3
def multiply_digits(n):
    if n <= 9:
        return n
    product = 1
    for digit in str(n):
        product *= int(digit)
    return multiply_digits(product)

n = int(input().strip())
print(multiply_digits(n))