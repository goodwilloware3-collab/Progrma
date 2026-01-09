squared=lambda num: num **2
print(squared(2))
add_two= lambda x: x+2
print(add_two(3))
add=lambda a,b: a+b
print(add(2,100))
def func_builder(x):
    return lambda num: num + x
add_ten=func_builder(10)
add_twenty=func_builder(20)
print(add_ten(7))
print(add_twenty(7))
numbers=[3,7,12,18,20,21]
squuared_nums=map(lambda x: x**2, numbers)
print(list(squuared_nums))
odd_nums=filter(lambda num:num%2 !=0, numbers)
print(list(odd_nums))
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)