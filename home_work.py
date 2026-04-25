#Ex 5.1

from string import digits, punctuation, digits
from keyword import kwlist

user_var = input('Enter you variable example: ')
prohibited_symbol = punctuation.replace('-', ' ')

is_contain_prohibited_symbol = False
is_contain_uppercase = False
is_contain_prohibited_symbols = False
for char in user_var:
    if char.isupper():
        is_contain_uppercase = True
        continue
    if char in prohibited_symbol:
     is_contain_prohibited_symbols = True
is_var_acceptable = (not user_var[0] in digits and not is_contain_uppercase and not is_contain_prohibited_symbols
                     and not user_var in kwlist and not '__' in user_var)
print(f'Is our {user_var} variable is acceptable? {is_var_acceptable}')

#Ex 5.2
def calculator():
    print("Welcome to the calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: invalid input")
            continue
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: division by zero!")
                continue
        else:
            print("Unknown operation")
            continue
        print(f"Result: {num1} {operation} {num2} = {result}")
        while True:
            choice = input("Do another? (y/n): ").strip().lower()
            if choice == 'y' or choice == 'yes':
                break
            elif choice == 'n' or choice == 'no':
                print("Thank you!")
                return
            else:
                print("Please enter y or n")
if __name__ == '__main__':
    calculator()

#ex 5.3
import string

def make_hashtag(text):
    for p in string.punctuation:
        text = text.replace(p, ' ')
    words = text.split()
    capitalized = [word.capitalize() for word in words]
    result = '#' + ''.join(capitalized)
    if len(result) > 140:
        result = result[:140]
    return result

if __name__ == '__main__':
    user_input = input("Enter a string: ")
    print(make_hashtag(user_input))
