# Ex 1
lst = [1, 2, 3, 4, 5]

if not lst:
    print("List is empty")
else:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]
    print(result)
 # Ex 2

lst = [12, 3, 4, 10]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
# Ex 3

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter operation +, -, *, /: ")
result = 0
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        result = "You can't divide by zero"
    else:
        result = first_number / second_number
else:
    result = "Invalid operation"
print(result)

