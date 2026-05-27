 #12.1
def prime_generator(end):
    for num in range(2, end + 1):
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            yield num
 #12.2
def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1
 #12.3
def is_even(number):
    return (number & 1) == 0
