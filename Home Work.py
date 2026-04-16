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

a = 3
b = 4
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
a = float(input("1: "))
b = float(input("5: "))
if b != 0:
    c = a / b
    print(c)
else:
    print("Деление на 0 нельзя ! ")
