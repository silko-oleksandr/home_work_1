# Ex 4.3
import random
length = random.randint(3, 10)
original_list = [random.randint(1, 100) for _ in range(length)]
new_list = [original_list[0] ,
original_list[2], original_list[-2]]
print(f"{original_list} == {new_list}")

#Ex 4.2
def sum_even_index_multiply_last(arr) :
    if not arr:
        return 0
    sum_even = sum( arr[i] for i in range(0,len(arr), 2))
    return sum_even * arr[-1]
print (sum_even_index_multiply_last([0, 1, 7, 2, 4, 8]))
print (sum_even_index_multiply_last([1, 2, 3,  5,]))
print (sum_even_index_multiply_last([6]))
print (sum_even_index_multiply_last([]))

#Ex 4.1
def move_zeros_to_end(lst) :
  non_zeros = [x for x in lst if x != 0]
  zeros_count = lst.count(0)
  return non_zeros + [0] * zeros_count
print (move_zeros_to_end([0, 1, 0, 12, 3]))
print (move_zeros_to_end([0]))
print (move_zeros_to_end([1, 0, 13, 0, 0, 5]))
print (move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]))
